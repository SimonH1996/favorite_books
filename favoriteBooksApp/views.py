from urllib import request
from django.shortcuts import redirect, render
from .models import Book
from userApp.models import User
# there are no constant variables in python 
# a work around is to write the variable in just capital letters to show others that this is a Const variable
# or writing like a method to make it not changeable
INDEX = 'favoriteBooksApp/index.html'

def isUserInList(request,list):
    for user in list:
        if user.email == request.session['user']:
            return True
 
    return False

def dashboard_view(request):
    context = {
        'books':Book.objects.all(),
        
    }
    return render(request,INDEX,context)


def create_book(request):
    book = Book.objects.create(
    title=request.POST['title']
    ,description=request.POST['description'],
    created_by=request.session['user'])
    book.user_who_liked.add(User.objects.get(email=request.session['user']))
    return redirect("/favBooksApp/")


def detail_view(request,book_id):
    context = {
        'book': Book.objects.get(id = book_id)
    }
    return render(request,"favoriteBooksApp/detail.html",context)

# Book.objects.get(id=book_id).update() isn´t working. 
# Also possible for updating: 
#                book = Book.objects.get(id = boo_id)
#                book.title = request.POST['title]
#                ....
#                book.save()
    
def update_book(request,book_id):
        Book.objects.filter(id=book_id).update(
            title=request.POST['title'],
            description = request.POST['description']
        )
        return redirect("/favBooksApp/detail/"+str(book_id))

def delete_book(request,book_id):
    Book.objects.get(id = book_id).delete()
    return redirect("/favBooksApp/")

# this function renders the detail page when the user isn´t logged in
def notLogin_View(request,book_id):

    userIn = isUserInList(request,Book.objects.get(id=book_id).user_who_liked.all())
    users_who_liked = Book.objects.get(id = book_id).user_who_liked.all()

    context = {
        'book': Book.objects.get(id = book_id),
        'user_who_liked': users_who_liked,
        'userIn': userIn
    }
    return render(request,"favoriteBooksApp/notLoginDetail.html",context)

#this function is triggered when a User want to add a book to their favourites
def favorBook(request,book_id):
    Book.objects.get(id = book_id).user_who_liked.add(User.objects.get(email = request.session['user']))
    return redirect("/favBooksApp/")




