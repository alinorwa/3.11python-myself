from django.urls import path
from .views import *



urlpatterns = [
    path('admin/' , admin , name='admin'),
    path('' , home , name='home'),
    path('create_post/' , create_post , name='create_post'),
    path('detail/<int:id>' , detail , name='detail'),
    path('update/<int:id>/' , update , name='update'),
    path('delete/<int:id>/' , delete , name='delete'),
]