from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    update_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.name


class Site(models.Model):
    children = models.ForeignKey("Link", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)
