from django.urls import path
from .views import index, by_rubric, BoardCreateView


urlpatterns = [
    path('', index, name="index"),
    path("<int:rubric_id>/", by_rubric, name="by_rubric"),
    path("add/", BoardCreateView.as_view(), name="add"),
]
