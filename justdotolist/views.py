from django.http import HttpResponseRedirect
from django.views import generic
from .models import BlogPost
from django.shortcuts import render
from .forms import UserForms


class BlogPost(generic.ListView):
    queryset = BlogPost.objects.all()
    context_object_name = 'blog_list'
    template_name = 'index.html'


def register(request):
    form = UserForms
    return render(request = request,
                  template_name = 'register.html',
                  context={"form": form})



