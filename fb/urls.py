from django.urls import path, include

from fb.views import index

urlpatterns = [
    path('', index, name='index'),
]
