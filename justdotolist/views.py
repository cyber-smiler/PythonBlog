from django.views import generic
from .models import BlogPost
from django.shortcuts import render


class BlogPost(generic.ListView):
    queryset = BlogPost.objects.all()
    context_object_name = 'blog_list'
    template_name = 'index.html'

# def blog_post(request):
#    blogs = BlogPost.objects.all()
#    return render(request, 'index.html', {'blog_list': blogs})



