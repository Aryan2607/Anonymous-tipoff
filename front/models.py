from django.db import models
from django.utils import timezone

# Create your models here.
class Tipoff(models.Model):
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=6)
    Nature_of_Incidence = models.CharField(max_length=100)
    Existing_or_Other = models.CharField(max_length=20)
    Listed_Cases = models.CharField(max_length=20)
    Message = models.TextField(max_length=5000)
    File_Uploaded = models.FileField(upload_to='documents/%Y/%m/%d')
    Gender = models.CharField(max_length=50)
    Mother_Tongue = models.CharField(max_length=50)
    Age = models.CharField(max_length=20)
    Educational_Qualification = models.CharField(max_length=50)
    Got_Information_About_Case = models.CharField(max_length=50)
    Relation_to_Suspect_or_Victim = models.CharField(max_length=50)
    Death_or_Loss_in_Family = models.CharField(max_length=10)
    Family_Member_is_not_healthy = models.CharField(max_length=10)
    Disruption_of_Intimate_Relationships = models.CharField(max_length=10)
    Faced_any_Violence = models.CharField(max_length=10)
    Disruption_in_Studies = models.CharField(max_length=10)
    Provided_information_to_Police_or_Justice_System = models.CharField(max_length=10)
    ip = models.CharField(max_length=20)

# The code below gives the option to make the case Active or Inactive and provide timezone
    is_active = models.IntegerField(default = 1,
                                   blank = True,
                                    null = True,
                                    help_text ='1->Active, 0->Inactive', 
                                    choices =(
                                    (1, 'Active'), (0, 'Inactive')
                                    ))
    created_on = models.DateTimeField(default = timezone.now)
    updated_on = models.DateTimeField(default = timezone.now,
                                    null = True, 
                                    blank = True
                                    )