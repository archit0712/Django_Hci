from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

tasks = ['hey', 'hello', 'bye']
# posts = [
#     {
#         'author': 'Anna',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date': 'August 10, 2020'
#     },
#     {
#         'author': 'Jane',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date': 'August 1, 2020'
#     }
# ]
def blog_index(request):
    context= {
        'posts' : Post.objects.all()
    }
    return render(request, 'blogs/index.html', context)

def tasks_index(request):
    return render(request, "tasks/index.html", {
        'tasks' : tasks
    })


def about(request):
    return HttpResponse('<h1>About Me</h1>')

def greet(request ,name):
    return HttpResponse(f"Hello, {name.capitalize()}!")