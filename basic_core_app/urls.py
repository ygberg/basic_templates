from django.conf.urls import url
from basic_core_app import views


#TEMPLATE TAGGING

app_name = 'basic_core_app'

urlpatterns = [
    url(r'^about/$',views.about, name='about'),
    url(r'^skills/$',views.skills, name='skills'),
    url(r'^projects/$',views.projects, name='projects'),

]
