from django.contrib import admin
from django.urls import include, path

from chat import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("chat/<str:room_name>/", views.room, name="room"),
]