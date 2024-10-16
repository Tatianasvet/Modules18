from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home_page.html')


def catalog(request):
    title = 'Книги'
    books = ['Дюна',
             'Мессия Дюны',
             'Дети Дюны',
             'Бог-Император Дюны',
             'Еретики Дюны',
             'Капитул Дюны']
    context = {'title': title,
               'books': books}

    return render(request, 'catalog.html', context)


def my_books(request):
    return render(request, 'my_books.html')
