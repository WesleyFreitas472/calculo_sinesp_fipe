from django.conf.urls import url
from .views import *

urlpatterns = [
	url('teste/',CalculaFipe.as_view())
]