from django.urls import include, path, re_path
from rest_framework import routers                    # add this
from .import views

router = routers.DefaultRouter()                      # add this
router.register(r'home', views.TodoView, 'todo')

urlpatterns = [
    path('', include(router.urls))
]