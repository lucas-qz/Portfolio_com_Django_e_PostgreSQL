from django.urls import path
from . import views as vw
urlpatterns = [
    path('',vw.portfolio,name='portfolio'),
    path('portfolio2',vw.portfolio2,name='portfolio2'),
    path('email',vw.email,name='email'),   
    path('r/<id>',vw.r,name='r'),   
]