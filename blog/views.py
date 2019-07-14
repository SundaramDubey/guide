from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import CreateView, ListView , DetailView,UpdateView,DeleteView
from .models import Article
from .forms import ModelArticleForm	
from django.urls import reverse 
from django.db.models import Q
import operator
from django.contrib.auth.decorators import login_required


#CLASS BASED VIEWS...
# WE ALSO CALL IT GENERIC VIEWS..


 
class ArticleCreateView(CreateView):
	form_class = ModelArticleForm
	template_name = "blog/article_create.html"
	queryset = Article.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)
	


class ArticleListView(ListView):
	template_name = "blog/article_list.html"
	queryset = Article.objects.all()

	 


class ArticleDetailView(DetailView):
	# id = pk but we have to use pk as default....
	template_name = "blog/article_detail.html"
	queryset = Article.objects.all()

	# to override its primary functions use get object ...
	def get_object(self):
		id_ =  self.kwargs.get("id")
		return get_object_or_404(Article, id =  id_)




class ArticleUpdateView(UpdateView):
	form_class = ModelArticleForm
	template_name = "blog/article_create.html"
	queryset = Article.objects.all()

	# to override its primary functions use get object ...
	def get_object(self):
		id_ =  self.kwargs.get("id")
		return get_object_or_404(Article, id =  id_)


	def form_valid(self, form):

		print(form.cleaned_data)
		return super().form_valid(form)
	

class ArticleDeleteView(DeleteView):
	template_name = "blog/article_delete.html"
	queryset =  Article.objects.all()

	def get_object(self):
		id_ =  self.kwargs.get("id")
		return get_object_or_404(Article, id =  id_)


	def get_success_url(self):
		return reverse('article-list')

def search(request):
	 template = 'blog/search.html'
	 query = request.GET.get('q')
	 if query:
	 	results = Article.objects.filter(Q(article_name__icontains= query) | Q(author__icontains = query) | Q(area__icontains = query))
	 else:
	 	results = Article.objects.all()
	 context = {
	 		"items":results
	 } 
	 return render(request, 'blog/search.html', context)