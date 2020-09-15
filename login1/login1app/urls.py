from django.conf.urls import url
from login1app import views

app_name='login1app'

urlpatterns=[
 url(r'^regi/$',views.register,name='register'),

]
