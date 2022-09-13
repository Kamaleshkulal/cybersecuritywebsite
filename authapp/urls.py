from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from authapp import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('buy',views.buynow,name="buynow"),
    path('contact',views.contact,name="contact"),
    path('services',views.handleservices,name="handleservices"),
    path('about',views.handleabout,name="handleabout"),
    path('buylater',views.buylater,name="buylater"),
    path('buyimmediate',views.buyimmediate,name="buyimmediate"),
    path('logout',views.handlogout,name="handlogout"),
    path('home',views.handlehome,name="handlehome"),
    path('payment',views.payment,name="payment"), 
    path('session',views.sessions,name="sessions"),
    path('award',views.awards,name="awards"),
    path('project',views.project,name="project"),
    path('internship',views.internship,name="internship"),
    path('handlecontact',views.handlecontact,name="handlecontact")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)