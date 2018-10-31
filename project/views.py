from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "project/project_list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['project_list_reverse'] = Project.objects.all().order_by("-init_date")
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/project_detail.html"
