from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic import View
# Create your views here.

def signup_view(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			form.save()
			return redirect('http://127.0.0.1:8000/register/')

	else:
		form = UserCreationForm()
	return render(request, 'signup.html',{'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			return redirect('http://127.0.0.1:8000/home/')

	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})

class UserFormView(View):
	form_class = UserForm
	template_name = 'signup_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user =  form.save(commit = False)
			# cleaned normalize
			username = form.cleaned_data['username']
			password  = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username = username,password = password)
			if(user is not None):
				login(request,user)
				return redirect('http://127.0.0.1:8000/register/')
		return render(request,'signup_form.html', {'form':form})