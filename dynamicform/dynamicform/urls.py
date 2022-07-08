from django.urls import path
from .views import create_formdata, done_form

app_name = 'dynamicform'

urlpatterns = [
    path('userform/', create_formdata, name='userform'),
    path('done/', done_form, name='done_form')
]
