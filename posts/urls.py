from django.urls import path
from . import views


urlpatterns = [
    path("", views.posts_list)
]


# http://127.0.0.1:8000/posts