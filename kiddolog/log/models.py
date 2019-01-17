from django.db import models
from django.urls import reverse # Used to generate urls by reversing the URL patterns 

class Kid(models.Model):
    """
    Model representing a kid with database
    """

    firstName = models.CharField(max_length=100, help_text="Enter first name of child.")
    lastName = models.CharField(max_length=100, help_text="Enter last name of child.")
    dob = models.DateField(help_text="Date of birth of child")
    
    class Meta:
        ordering = ["lastName","firstName"]

    def __str__(self):
        """
        String for representing the Model object
        """

        return self.lastName + ", " + self.firstName

    def get_absolute_url(self):
        """
        Returns the url to access a particular kid instance
        """

        return reverse('kid-detail', args=[str(self.id)])

class Caretaker(models.Model):
    """
    Model representing a caretaker with database
    """

    firstName = models.CharField(max_length=100, help_text="Enter first name of caretaker.")
    lastName = models.CharField(max_length=100, help_text="Enter last name of caretaker.")
    kid_id = models.ForeignKey('Kid', on_delete=models.SET_NULL, null=True, help_text="Enter the kid that the caretaker is watching.")
    
    class Meta:
        ordering = ["lastName","firstName"]

    def __str__(self):
        """
        String for representing the Model object
        """

        return self.lastName + ", " + self.firstName

    def get_absolute_url(self):
        """
        Returns the url to access a particular kid instance
        """

        return reverse('caretaker-detail', args=[str(self.id)])

class Log(models.Model):
    """
    Model representing a log of an event for a child within the database
    """

    ACTIVITY_TYPE = (
        ('t', 'toilet'),
        ('r', 'rest'),
        ('m', 'meal'),
        ('a', 'activity'),
        ('o', 'other'),
        ('d', 'dropoff'),
        ('p', 'pickup'),
        ('c', 'check'),
        ('n', "notes to parents")
    )

    kid = models.ForeignKey('Kid', on_delete=models.SET_NULL, null=True)
    date = models.DateField(help_text="Date of log item.")
    time = models.TimeField(help_text="Time of log item.")
    activity = models.CharField(max_length=1, choices=ACTIVITY_TYPE, blank=False,
                                help_text='Type of activity.')
    description = models.CharField(max_length=1000, help_text="Description of log item.", blank=False)
    
    class Meta:
        ordering = ["-date","-time"]

    def __str__(self):
        """
        String for representing the Model object
        """

        return self.date.strftime('%y/%m/%d') + " " + self.time.strftime("%I:%M %p") + " " + self.activity + " " + self.description[:40]









































