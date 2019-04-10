from django.shortcuts import render
from .forms import PostModelForm

# Create your views here.
def create(request):
    # post를 작성하는 form을 가져와 template에서 보여줌
    if request.method == 'POST':
        pass
    else:
        form = PostModelForm()
        context = {
            'form': form,
        }
        
        return render(request,'posts/create.html', context)