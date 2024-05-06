from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('buy/<int:pk>/',views.buy,name='buy'),
    path('pdf/',views.pdf,name='pdf'),
    path('about/',views.about,name='about'),
]