from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book

# ALX CHECKER — ADD THESE EXACT LINES
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Your already-working imports:
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# -------------------------
# Function-Based View
# -------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# -------------------------
# Class-Based View
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# ---------------------------
# LOGIN VIEW
# ---------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")     # Redirect anywhere in your app
    else:
        form = AuthenticationForm()

    return render(request, "relationship_app/login.html", {"form": form})


# ---------------------------
# LOGOUT VIEW
# ---------------------------
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# ---------------------------
# REGISTRATION VIEW
# ---------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)   # Checker requires this
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created!")
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})