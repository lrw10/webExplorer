from django.forms import Form, URLField


class SearchForm(Form):
    url = URLField(max_length=200)
