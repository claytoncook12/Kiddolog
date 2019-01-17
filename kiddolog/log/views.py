from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import path, reverse
from django.forms import ModelForm
from datetime import datetime, timedelta

from .models import Kid, Caretaker, Log
from .forms import NewLog, EditLog

# Create your views here.
def index(request):

	return render(request, 'index.html')

def about(request):

	return render(request, 'about.html')

class KidListView(LoginRequiredMixin, generic.ListView):

	model = Kid

class KidDetailView(LoginRequiredMixin, generic.DetailView):

	model = Kid

@login_required
def DateListView(request, pk, date):

	base_url = reverse("kid-detail", kwargs={"pk": pk})

	kid_name = Kid.objects.filter(id=pk).first()
	kid_name = kid_name.firstName + " " + kid_name.lastName

	kid_log_day = Log.objects.filter(kid_id=pk).filter(date=date).order_by('time')

	day_of_week = datetime.strptime(date, "%Y-%m-%d")
	day_of_week = day_of_week.strftime("%A")

	previous_day = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)
	previous_day = previous_day.strftime('%Y-%m-%d')

	next_day = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
	next_day = next_day.strftime('%Y-%m-%d')

	# If this is a POST request then process the Form data
	if request.method == 'POST':

		form = NewLog(request.POST)

		if form.is_valid():
			form.save()
			return_url = str(reverse('date-detail', args=(pk,date,)))
			response = redirect(return_url)
			return response

	# If this is a GET (or any other method) create the default form
	else:

		form = NewLog(initial={"kid": pk,"date": date, "time": datetime.now().strftime("%H:%M")})

	return render(request, 'log\kid_log_day.html', {"kid_log_day": kid_log_day, "kid_name": kid_name, "date": date, "pk":pk,
													"base_url": base_url, "previous_day": previous_day, "next_day": next_day,
													"day_of_week":day_of_week, 'form':form,})

@login_required
def delete_log(request, pk):

	# Deleting Specific Log From Database
	Log.objects.get(id=pk).delete()

	# Construct Redirecting URL once data is deleted
	kid_id = request.GET.get('kid_id', '')
	day = request.GET.get('date','')
	return_url = str(reverse('date-detail', args=(kid_id,day,)))
	response = redirect(return_url)

	return response

@login_required
def edit_log(request, pk):

	# Construct Redirecting URL once data is updated succesfully
	kid_id = request.GET.get('kid_id', '')
	day = request.GET.get('date','')
	return_url = str(reverse('date-detail', args=(kid_id,day,)))
	response = redirect(return_url)

	log_entry = get_object_or_404(Log, pk=pk)
	form = EditLog(request.POST or None, instance=log_entry)
	
	if form.is_valid():
		form.save()
		return response

	return render(request, 'log/log_edit.html', {'form':form, 'return_url':return_url})