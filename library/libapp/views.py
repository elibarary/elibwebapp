from .models import BooksModel , FeedBack , BestBooks , OtherModel,SearchModel,ThesisModel , FileModel
from .serializers import BooksSerializer , FeedBackSerializer , UserSerializer , ThesisSerializer , OtherSerializer , SearchSerializer
from rest_framework import viewsets
from django.shortcuts import render , get_object_or_404 , redirect
from .fillters import BooksFilter
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FeedCreateForm

class BooksList(viewsets.ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = [IsAdminUser]

class OtherList(viewsets.ModelViewSet):
    queryset = OtherModel.objects.all()
    serializer_class = OtherSerializer

class SearchList(viewsets.ModelViewSet):
    queryset = SearchModel.objects.all()
    serializer_class = SearchSerializer

class ThesisList(viewsets.ModelViewSet):
    queryset = ThesisModel.objects.all()
    serializer_class = ThesisSerializer

class FeedBackList(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    # permission_classes = [IsAdminUser]
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]


def webinfo(request):
    return render(request,'websiteinfo.html',{})

def Home(request):
    images = BestBooks.objects.all()
    return render(request,'home.html',{
        "images":images,
        })


def books(request):


	books  = BooksModel.objects.all()
	files  = FileModel.objects.all()
	images = BestBooks.objects.all()
	book_number= BooksModel.objects.all().count()

	query = request.GET.get("q")
	if query:
	    books = books.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(speciality__icontains=query)).distinct()
	paginator = Paginator(books, 15)
	books_filters = BooksFilter(request.GET,queryset=books)
	page = request.GET.get('page')
	try:
	    books = paginator.page(page)
	except PageNotAnInteger:
	    books = paginator.page(1)
	except EmptyPage:
	    books = paginator.page(paginator.num.page)
	context = {
	  'book_number':book_number,
	'q':query,
    "books":books,
    "images":images,
    'filters': books_filters,
    'page': page,
    'files':files

	}
	return render(request,"books.html",context)

def search(request):


	searches = SearchModel.objects.all()
	images = BestBooks.objects.all()
	book_number= SearchModel.objects.all().count()
	query = request.GET.get("q")
	if query:
	    books = books.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(speciality__icontains=query)).distinct()
	paginator = Paginator(searches, 15)
	books_filters = BooksFilter(request.GET,queryset=searches)
	page = request.GET.get('page')
	try:
	    searches = paginator.page(page)
	except PageNotAnInteger:
	    searches = paginator.page(1)
	except EmptyPage:
	    searches = paginator.page(paginator.num.page)
	context = {
	'book_number':book_number,
	'q':query,
    "searches":searches,
    "images":images,
    'filters': books_filters,
    'page': page,

	}
	return render(request,"search.html",context)


def other(request):


	others = OtherModel.objects.all()
	images = BestBooks.objects.all()
	other_number= OtherModel.objects.all().count()
	query = request.GET.get("q")
	if query:
	    books = books.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(speciality__icontains=query)).distinct()
	paginator = Paginator(others, 15)
	books_filters = BooksFilter(request.GET,queryset=others)
	page = request.GET.get('page')
	try:
	    others = paginator.page(page)
	except PageNotAnInteger:
	    others = paginator.page(1)
	except EmptyPage:
	    others = paginator.page(paginator.num.page)
	context = {
	   'other_number':other_number,
	 'q':query,
    "others":others,
    "images":images,
    'filters': books_filters,
    'page': page,

	}
	return render(request,"other.html",context)


def thesis(request):


	thesises = ThesisModel.objects.all()
	images = BestBooks.objects.all()
	thesis_number= ThesisModel.objects.all().count()
	query = request.GET.get("q")
	if query:
	    books = books.filter(Q(title__icontains=query)|Q(author__icontains=query)|Q(speciality__icontains=query)).distinct()
	paginator = Paginator(thesises, 15)
	books_filters = BooksFilter(request.GET,queryset=thesises)
	page = request.GET.get('page')
	try:
	    thesises = paginator.page(page)
	except PageNotAnInteger:
	    thesises = paginator.page(1)
	except EmptyPage:
	    thesises = paginator.page(paginator.num.page)
	context = {
	    'thesis_number':thesis_number,
	 'q':query,
    "thesises":thesises,
    "images":images,
    'filters': books_filters,
    'page': page,

	}
	return render(request,"thesis.html",context)


class FeedCreateView(LoginRequiredMixin, CreateView):
    model = FeedBack
    # fields = ['title', 'content']
    template_name = 'newfeed.html'
    form_class = FeedCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def Book(request, book_id):
    book = get_object_or_404(BooksModel, pk=book_id)
    files  = FileModel.objects.all()



    context = {
        'files':files,
        'title': book,
        'book': book,


    }

    return render(request, 'detail.html', context)

def Searchd(request, search_id):
    search = get_object_or_404(SearchModel, pk=search_id)
    files  = FileModel.objects.all()



    context = {
        'files':files,
        
        'search': search,


    }

    return render(request, 'details.html', context)



def Otherd(request, other_id):
    other = get_object_or_404(OtherModel, pk=other_id)
    files  = FileModel.objects.all()



    context = {
        'files':files,
        
        'other': other,


    }

    return render(request, 'detailo.html', context)

def Thesisd(request, thesis_id):
    thesis = get_object_or_404(ThesisModel, pk=thesis_id)
    files  = FileModel.objects.all()



    context = {
        'files':files,
        
        'thesis': thesis,


    }

    return render(request, 'detailt.html', context)



def Feeds(request):
    feeds = FeedBack.objects.all()
    paginator = Paginator(feeds, 15)
    page = request.GET.get('page')
    try:
        feeds = paginator.page(page)
    except PageNotAnInteger:
        feeds = paginator.page(1)
    except EmptyPage:
        feeds = paginator.page(paginator.num.page)
    context = {
    "feeds":feeds,
    'page': page,}
    return render(request,"feeds.html",context)

def logout_user(request):
    logout(request)
    return redirect('home')






def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')

    return render(request, 'login.html', {
        'title': 'تسجيل الدخول',
    })




