from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
 path('',views.form,name='form'),
  path('stud',views.stud,name='stud'),
  path('table',views.table,name='table'),

]
