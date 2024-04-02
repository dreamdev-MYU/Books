from django.urls import path
from .views import books_page, about,all_reviews,AddCommentView
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', books_page, name='books_page'),
    path('about/<int:id>/', about, name='about_page'),  
    path('all_reviews/', all_reviews, name='all_reviews'), 
    path('add_comment/<int:id>/',AddCommentView.as_view(), name='add_comment'),  

    path('uzbek/', views.uzbek_books_view, name='uzbek_books'),
    path('english/', views.english_books_view, name='english_books'),
    path('russian/', views.russian_books_view, name='russian_books'),
    path('category/<int:category_id>/', views.category_books_view, name='category_books'),
    
]
