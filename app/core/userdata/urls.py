from django.urls import path
from . import views

urlpatterns = [
    path ('nosotros/',views.NosotrosPageView.as_view(), name='nosotros'),
]