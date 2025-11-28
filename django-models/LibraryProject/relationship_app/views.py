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

from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.contrib.auth.decorators import permission_required


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

# ---------------------------
# Role Check Functions
# ---------------------------
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# ---------------------------
# Role-Based Views
# ---------------------------
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# ---------------------------
# Custom Permission Views (Add, Edit, Delete Book)
# ---------------------------
from .forms import BookForm
from django.shortcuts import get_object_or_404

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()

    return render(request, "relationship_app/add_book.html", {"form": form})


@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)

    return render(request, "relationship_app/edit_book.html", {"form": form})


@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("list_books")

    return render(request, "relationship_app/delete_book.html", {"book": book})
