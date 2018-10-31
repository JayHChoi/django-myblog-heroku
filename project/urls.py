from django.urls import path
from .views import ProjectListView, ProjectDetailView

app_name = 'project'
urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='detail'),
]
