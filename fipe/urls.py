from django.conf.urls import url
from .views import *

urlpatterns = [
	url('consulta/',CalculaFipe.as_view())
]
