from django.db import models
# Create your models here.

class Contact_Us_Feedback:
    info_type=models.CharField(max_length=None)
    Fullname_ursername=models.CharField( max_length=50)
    Email=models.EmailField()
    Issue_quriy=models.TextField()

class Contact_Us_Issues:
    info_type=models.CharField(max_length=None)
    Fullname_ursername=models.CharField( max_length=50,blank=False)
    Email=models.EmailField(blank=False)
    Issue_quriy=models.TextField(blank=False)

class Contact_Us_Quiry:
    info_type=models.CharField(max_length=None)
    Fullname_ursername=models.CharField( max_length=50)
    Email=models.EmailField()
    Issue_quriy=models.TextField()
