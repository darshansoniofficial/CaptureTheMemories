from django.urls import path, include
from . import views

 
urlpatterns = [
    path('',views.index,name="homepage"),
    path('about/',views.about,name="aboutpage"),
    path('contact/',views.contact,name="contactpage"),
    path('photography/',views.single, name="photography"),
    path('<slug:categoryid>',views.category,name="category"),
    path('<slug:categoryid>/<slug:photoid>',views.download,name="download")
   
]
