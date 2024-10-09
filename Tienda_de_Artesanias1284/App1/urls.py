from django.urls import path
from App1.views import IndexView, ProvedorView


urlpatterns = [
    path('', IndexView),
    path("provedor/<int : id>", ProvedorView)
]