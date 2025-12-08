from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

MENU = {"главная":"/", "О блоге":"/about", "пост":"/post", }


def main_page(request):

    data = {"menu":MENU}
    return render(request, "./index.html", context=data)

def about_page(request, topic = 'Main'):
    title = "О блоге"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)

def post_page(request, id = 1):
    title = "Поcт"
    data = {"menu": MENU, "title": title}
    return render(request, "./post.html", context=data)

def reviews_page(request):
    reviews = Review.objects.filter(checked=True)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews_page")
    else:
        form = ReviewForm()

    return render(request, "reviews.html", {"reviews": reviews, "form": form})
