from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post

# Create your views here.
def create(request):
    # post를 작성하는 form을 가져와 template에서 보여줌
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
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
    
def delete(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    post.delete()
    return redirect('posts:list')
    
def update(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'posts/create.html', {'form': form})