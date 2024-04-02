from django.shortcuts import render, get_object_or_404, redirect
from .models import Books,Comment, Category
from .forms import BooksCommentForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin




def category_books_view(request, category_id):
    category = Category.objects.get(id=category_id)
    books_in_category = category.books_set.all()  
    return render(request, 'books/category_books.html', {'category': category, 'books': books_in_category})


def books_page(request):
    english_books = Books.objects.filter(language='en')
    russian_books = Books.objects.filter(language='ru')
    uzbek_books = Books.objects.filter(language='uz')
    
    books = list(english_books) + list(russian_books) + list(uzbek_books)
    
    search_query = request.GET.get('q', '')
    if search_query:
        books = Books.objects.filter(name__icontains=search_query)
    
    return render(request, 'books/books.html', {"books": books, "search_query": search_query})



def uzbek_books_view(request):
    uzbek_books = Books.objects.filter(language='uz')
    return render(request, 'books/uzbek_books.html', {'uzbek_books': uzbek_books})

def english_books_view(request):
    english_books = Books.objects.filter(language='en')
    return render(request, 'books/english_books.html', {'english_books': english_books})
    


def russian_books_view(request):
    russian_books = Books.objects.filter(language='ru')
    return render(request, 'books/russian_books.html', {'russian_books': russian_books})






def about(request, id):    
    book = get_object_or_404(Books, pk=id)
    if request.method == 'POST':
        form = BooksCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            
            comment.user = request.user
            comment.save()
            return redirect('books:about_page', id=id)  
    else:
        form = BooksCommentForm()
    return render(request, 'books/about.html', {'book': book, 'form': form})



def all_reviews(request):
    all_reviews = Comment.objects.all()
    return render(request, 'books/all_reviews.html', {'all_reviews': all_reviews})





class AddCommentView(LoginRequiredMixin, View):
    def get(self, request, id):
        book = get_object_or_404(Books, pk=id)
        form = BooksCommentForm()
        return render(request, 'books/about.html', {'book': book, 'form': form})

    def post(self, request, id):
        book = get_object_or_404(Books, pk=id)
        form = BooksCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            
            comment.user = request.user
            comment.save()
            return redirect(reverse("books:about_page", kwargs={"id": book.id}))
        return render(request, 'books/about.html', {'book': book, 'form': form})

@login_required
def add_comment(request, book_id):
    if request.method == 'POST':
        user_id = request.user.id  
        comment_text = request.POST.get('comment_text')
    
        comment = Comment.objects.create(user_id=user_id, book_id=book_id, comment_text=comment_text)
       
        return redirect('book_detail', book_id=book_id)  
    else:
        return redirect('book_detail', book_id=book_id) 