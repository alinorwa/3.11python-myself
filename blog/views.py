
from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms import CreateForm
from django.contrib.auth.decorators import login_required

# admin 
def admin(request):
    return redirect('admin')

# get all post
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request , 'home.html' , context)


# create post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = CreateForm()  

   

    context = {
        'form': form
    }
    return render(request , 'create_post.html' , context)


# get post by id
def detail(request, id):
    post = get_object_or_404(Post , pk=id)
    context = {
        'post' : post
    }
    return render(request , 'detail.html' , context)


     

def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('detail', post.id)
            # return redirect('home')
    else:
        form = CreateForm(instance=post)
    return render(request, 'update.html', {'form': form , 'post':post})



# delete 
def delete(request , id):
    post = get_object_or_404(Post , pk=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request , 'delete.html' , {'post' : post})
