from multiprocessing import context
from django.shortcuts import render

from core.models import Post

# Create your views here.
def index(request):
    posts=Post.objects.all()
    
    context={
        'posts': posts,
    }
    return render(request,'core/index.html',context)