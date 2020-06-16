from django.shortcuts import render,redirect
from .forms import product_form
from .models import Post
# Create your views here.

def home_view(request):
	return render(request,'home.html',{})


def create_post_view(request):
	my_form = product_form(request.POST or None)

	if request.method == "POST":
		if my_form.is_valid():
			my_form.save()
			my_form = product_form()
			return redirect("/")

	context = {
	'form' : my_form
	}

	return render(request,'create.html',context)

def all_post_view(request):
	obj = Post.objects.all()
	context = {
	'post':obj
	}
	return render(request,'all_post.html',context)

def latest_post(request):
	obj = Post.objects.all()
	o = list(obj)
	new = o[-1]
	context = {
	'post':new
	}
	return render(request,'latest_post.html',context)

def one_post(request,id):
	obj = Post.objects.get(id = id)
	
	context = {
	'post':obj
	}
	return render(request,'one_post.html',context)