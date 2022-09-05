from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'rida',
        'title': 'blog post',
        'content':'this is my first post',
        'date_posted': 'september 5, 2022'
    },
    {
       'author': 'ayesha',
        'title': 'blog post two',
        'content':'another post',
        'date_posted': 'september 6, 2022' 
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})  
