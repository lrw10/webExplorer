from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "site/<int:site_id>/",
        views.site_detail,
        name="site_detail",
    ),
    path(
        "url/<int:url_id>/",
        views.url_detail,
        name="url_detail",
    ),
    path(
        "search/",
        views.search,
        name="search",
    ),
    path(
        "scan/",
        views.scan,
        name="scan",
    ),
]
