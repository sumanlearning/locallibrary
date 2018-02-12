from django.shortcuts import render
# from django.views import generic
from django.views.generic import ListView, DetailView
from catalog.models import Book

# Create your views here.
from .models import Book, Author, BookInstance, Genre, Language

def index(request):
	"""======view function ke home page====="""
	# generate count object
	num_books = Book.objects.filter(language__name__icontains='english').count()
	num_instances = BookInstance.objects.all().count()
	# buku yang available (status = 'a)
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()
	# session tracking, number of visits to this view, as coubted in the session variable
	num_visits=request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits+1
	num_genre = Genre.objects.count()
	print('index.html')

	# render html
	return render(request, 'index.html', 
		context={'num_books': num_books, 
				'num_instances': num_instances, 
				'num_instances_available': num_instances_available, 
				'num_authors': num_authors,
				'num_visits': num_visits},
				)	


class BookListView(ListView):
	model = Book
	paginate_by = 2

	print('booklistview class running')

	context_object_name = 'my_book_list'
	# queryset = Book.objects.filter(title__icontains='a')[:3]
	# template_name = 'books/my_arbitary_template_name_list.html'

	""" overridding methods in class-based viewa"""
	# def get_queryset(self):
	# 	return Book.objects.filter(title__icontains='ar')[:5]

	"""cara overridding yang lainnya """
	"""def get_context_data(self, **kwargs):
		# call the base implementation first to get context
		context = super(BookListView, self).get_context_data(**kwargs)
		# create any data and add it to the context
		context['some_data'] = 'This is just some data'
		return context"""
class BookDetailView(DetailView):
	model = Book
	print("book detail view")

class AuthorListView(ListView):
	model = Author
	paginate_by = 2
	context_object_name = 'my_author_list'
	print('class AuthorListView running')

class AuthorDetailView(DetailView):
	model = Author
	print('class AuthorDetailView is running')

