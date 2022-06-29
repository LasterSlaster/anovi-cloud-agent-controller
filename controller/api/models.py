from django.contrib.sites import requests
from django.db import models
from django.utils import timezone
import datetime


class Request(models.Model):
    request_content = models.CharField(max_length=10000)
    request_date = models.DateTimeField()
    response_content = models.CharField(max_length=10000)

    def __str__(self):
        return self.request_content

    def send(self):
        self.response_content = requests.get(self.request_content)
        self.request_date = timezone.now()
