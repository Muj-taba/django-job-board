
from django.urls import path
from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='home_page'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),

    ####### api urls #######

############ function based views ##########
    path('api/list', api.job_list_api, name='api_list'),
    path('api/add', api.job_add_api, name='job_add_api'),
    path('api/update/<id>', api.job_update_api, name='job_update_api'),
    path('api/delete/<id>', api.job_delete_api, name='job_delete_api'),
    path('api/<id>', api.job_detail_api, name='job_detail_api'),

############ Class based views ##########

    path('api/v2/list', api.JobListV2.as_view(), name='JobListV2'),
    path('api/v2/update/<id>', api.JobUpdateV2.as_view(), name='JobupdateV2'),
    path('api/v2/delete/<id>', api.JobDeleteV2.as_view(), name='JobDeleteV2'),



]

