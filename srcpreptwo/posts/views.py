from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostModelForm
from .models import Post
# Create your views here.

def post_create(request):
	form = PostModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form':form,
	}
	return render(request, 'post_form.html', context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostModelForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form':form,
	}
	return render(request, 'post_form.html', context)
def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		'title':'Post Detail',
		'instance':instance
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		'title':'List on its way',
		'queryset':queryset
	}
	return render(request, 'post_list.html', context)
	
def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return redirect('posts:list')

