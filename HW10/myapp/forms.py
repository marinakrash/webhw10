from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quote


class AuthorForm(ModelForm):
    name = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    description = CharField(max_length=50, null=False)

    class Meta:
        model = Author
        fields = ['name', 'description']


class QuoteForm(ModelForm):
    author = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    quote = CharField(max_length=50, null=False)

    class Meta:
        model = Quote
        fields = ['author', 'quote']
