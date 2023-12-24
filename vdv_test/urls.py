from django.urls import path

from .views import *


urlpatterns = {
    path('', get_projects),
    path('create/', crate_project),
    path('delete/<int:project_id>/', delete_project),
}