# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class host_info(models.Model):
    host_name = models.CharField(max_length=300)
    host_ip = models.CharField(max_length=20)

