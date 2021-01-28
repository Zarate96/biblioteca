from django.shortcuts import render,redirect
from .forms import AuthorForm
from .models import Author
# Create your views here.

def Home(request):
    return render(request, 'index.html', {'title':'Home'})

def createAuthor(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('home')
    else:
        author_form = AuthorForm()
    return render(request, 'book/createAuthor.html', {'author_form':author_form, 'title':'Create author'})

def listAuthor(request):
    authors = Author.objects.filter(estado=True)
    return render(request, 'book/list_author.html', {'authors':authors, 'title':'List author'})

def updateAuthor(request,id):
    author = Author.objects.get(pk=id)
    if request.method == 'GET':
        author_form = AuthorForm(instance=author)
    else:
        author_form = AuthorForm(request.POST, instance=author)
        if author_form.is_valid():
            author_form.save()
            return redirect('home')
    return render(request, 'book/createAuthor.html', {'author_form':author_form})

def deleteAuthor(request,id):
    author = Author.objects.get(pk=id)
    if request.method == 'POST':
        author.estado=False
        author.save()
        return redirect('book:listAuthor')
    return render(request,'book/deleteAuthor.html', {'author':author, 'title':'Delete Author'})
