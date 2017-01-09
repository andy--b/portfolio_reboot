from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^treenode$', views.treeNode, name='treeNode'),
]
