from django.shortcuts import render, get_object_or_404
from .models import Guides
from django.views.generic.list import ListView
from .forms import RegisterForm
import operator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from django.db.models import Q

# Create your views here.

def main(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return render(request,'login.html',{})
	else:
		queryset  = Guides.objects.all()
		context = {
				"object_list" : queryset,
		}
	return render(request, 'home.html',context)

def search(request):
	template = 'search.html'
	query = request.GET.get('q')
	if query:
		results = Guides.objects.filter(Q(area__icontains= query) | Q(name__icontains = query))
	else:
		results = Guides.objects.all()
	context = {
			"items":results
	} 
	return render(request, 'search.html', context)

def logout_user(request):
    logout(request)
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)

@login_required
def register(request):
	if not request.user.is_authenticated:
		return render(request, 'login.html',{})
	else:
		form = RegisterForm(request.POST or None)
		if form.is_valid():
			form.save()
			form = RegisterForm()

		context = {
				'form' : form
		}
	return render(request, 'create.html', context)

@login_required
def detail(request,id):
	if not request.user.is_authenticated:
		return render(request, 'login.html',{})
	else:
		obj = Guides.objects.get(id=id)
		context = {'object'  : obj}
	return render(request, "detail.html",context)