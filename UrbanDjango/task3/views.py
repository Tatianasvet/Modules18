from django.shortcuts import render
#from django.views.generic import TemplateView
# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')


def catalog(request):
    title = 'Книги'
    book1 = 'Дюна'
    book2 = 'Мессия Дюны'
    book3 = 'Дети Дюны'
    book4 = 'Бог-Император Дюны'
    book5 = 'Еретики Дюны'
    book6 = 'Капитул Дюны'
    context = {'title': title,
               'book1': book1,
               'book2': book2,
               'book3': book3,
               'book4': book4,
               'book5': book5,
               'book6': book6}
    return render(request, 'catalog.html', context)


def my_books(request):
    return render(request, 'my_books.html')
