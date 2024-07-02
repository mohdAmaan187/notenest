from django.urls import path
from notecrud_App import views
urlpatterns = [
    path('Home/',views.Home),
    path('Sign-In/',views.Signin),
    path('About-Us/',views.About),
    path('Contact-us/',views.Contact),
    path('Browse/',views.Browse),
]
