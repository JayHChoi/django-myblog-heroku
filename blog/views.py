from django.views.generic import ListView, DetailView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['blog_list_reverse'] = Blog.objects.all().order_by("-pub_date")
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
