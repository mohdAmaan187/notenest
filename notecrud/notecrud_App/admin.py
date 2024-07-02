from django.contrib import admin
from .models import Contact_Us_Feedback,Contact_Us_Issues,Contact_Us_Quiry

# Register your models here.
class Contact_For_Issues_Feedback_Quiry(admin.ModelAdmin):
    data=('info_type','Fullname_ursername','Email','Issue_quriy')

class Contact_For_Issues_Feedback_Quiry(admin.ModelAdmin):
    data=('info_type','Fullname_ursername','Email','Issue_quriy')

class Contact_For_Issues_Feedback_Quiry(admin.ModelAdmin):
    data=('info_type','Fullname_ursername','Email','Issue_quriy')

admin.site.register(Contact_Us_Feedback)
admin.site.register(Contact_Us_Issues)
admin.site.register(Contact_Us_Quiry)

