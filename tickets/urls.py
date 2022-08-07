from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.create_ticket),
    path("all/", views.get_tickets_all),
    path("markAsClosed/", views.close_ticket),
    path("delete/", views.delete_ticket),
    path("", views.get_tickets),
]
