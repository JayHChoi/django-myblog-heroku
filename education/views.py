from django.views.generic import ListView
from .models import Education


class EducationListView(ListView):
    model = Education
    template_name = "education/education_list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['education_list_reverse'] = Education.objects.all().order_by("-finish_date")
        return context
