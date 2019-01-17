from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('kids/', views.KidListView.as_view(), name='kids'),
	path('kids/<int:pk>', views.KidDetailView.as_view(), name='kid-detail'),
	path('kids/<int:pk>/<slug:date>', views.DateListView, name='date-detail'),
	path('log/edit/<int:pk>', views.edit_log, name="edit_log"),
	path('log/delete/<int:pk>', views.delete_log, name="delete_log"),
]