from django.urls import path
from . import views

urlpatterns = [
    # path('ratings', views.ratings),
    path('form', views.form_view, name='form'),
]
