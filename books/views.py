from django.shortcuts import render
from django.views import generic
from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import *
from .form import *


class BooksListView(generic.ListView):
    model = Book
    paginate_by = 6
    template_name = "books/book_list.html"
    context_object_name = "books"


# class BooksDetailView(generic.DetailView):
#     model = Book
#     template_name = "books/book_detail.html"
@login_required()
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()
    return render(request, "books/book_detail.html", {"book": book, "comments": book_comments, "comment_form": comment_form})
# ======================================================================================================


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ["title", "author", "description", "price", "cover", ]
    template_name = "books/book_create.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)

# class BookCreateView(LoginRequiredMixin, View):
#     def get(self, request):
#         post_form = BookForm()
#         return render(request, "books/book_create.html",
#                       {"form": post_form})
#
#     def post(self, request):
#         post_form = BookForm(request.POST)\
#
#         if post_form.is_valid():
#             post = post_form.save(commit=False)
#             post.user = request.user
#             post.cover = request.FILES.get("cover")
#             post.save()
#             return redirect("book_list")
#         return render(request, "books/book_create.html", {"form": post_form})
#=============================================================================================


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ["title", "author", "description", "price", "cover", ]
    template_name = "books/book_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

