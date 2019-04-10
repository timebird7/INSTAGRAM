from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post

# Create your views here.
def create(request):
    # post를 작성하는 form을 가져와 template에서 보여줌
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        form = PostModelForm()
        context = {
            'form': form,
        }
        
        return render(request,'posts/create.html', context)
        
def list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'posts/list.html', context)