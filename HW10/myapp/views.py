from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AuthorForm, QuoteForm
from .models import Author, Quote


def main(request):
    quote = Quote.objects.filter(user=request.user).all() if request.user.is_authenticated else []
    return render(request, 'myapp/index.html', {"quote": quote})

@login_required
def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, user=request.user)
    return render(request, 'myapp/detail.html', {"quote": quote})

@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='myapp:main')
        else:
            return render(request, 'myapp/author.html', {'form': form})

    return render(request, 'myapp/author.html', {'form': AuthorForm()})

@login_required
def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect(to='myapp:main')
        else:
            return render(request, 'myapp/quote.html', {'form': form})

    return render(request, 'myapp/quote.html', {'form': QuoteForm()})