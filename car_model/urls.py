from django.urls import path
from . import views


urlpatterns = [
    path('details/<int:id>',views.detailiView.as_view(),name='detail_page'),
]