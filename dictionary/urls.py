from django.urls import path

from .views import Detail, Index

app_name = "dictionary"
urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dictionaries/<str:source>/<slug:slug>", Detail.as_view(), name="detail"),
]
