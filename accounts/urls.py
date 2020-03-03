from django.urls import path
from .views import person_inquir ,login
from .import views

urlpatterns=[
    path('login/',views.login ,name='login'),
    path('',views.home, name='home'),
    path('inquiry', views.person_inquiry),
    path('logout/',views.logout),

]