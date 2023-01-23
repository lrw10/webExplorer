from django.shortcuts import render
from django.http import HttpResponse
from .models import Link, Site
from .forms import SearchForm
import urllib.request
import datetime
import re


def index(request):
    founded_sites_list = Site.objects.all()
    output = ", ".join([s.children.name for s in founded_sites_list])
    return HttpResponse(output)


def url_detail(request, url_id):
    return HttpResponse("You are looking at url %s." % url_id)


def site_detail(request, site_id):
    return HttpResponse("You are looking at site %s." % site_id)


"""
Scan a web page looking for urls
each founded url is opened and also scanned
"""


def page_scan(url):
    try:
        website = urllib.request.urlopen(url).read()
        url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
        children = re.findall(url_extract_pattern, str(website))  # Returns Match object
        for child in children:
            newLink = Link(url=child, name=child)
            newLink.update_date = datetime.datetime.now()
            query_result = Link.objects.filter(url=newLink.url)
            if not query_result:
                newLink.save()
                page_scan(newLink.url)
        return
    except Exception as e:
        print(e)

    return


"""
return the search page that allow user to enter the root url
"""


def search(request):
    search_form = SearchForm()
    return render(request, "webSearch/search.html", {"search_form": search_form})


"""
handle search requests
"""


def scan(request):
    if request.method == "POST":
        page_scan(request.POST["url"])
        return index(request)
    else:
        return index(request)
