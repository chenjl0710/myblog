# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.admin import User
# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()

    def __unicode__(self):
        return self.title


class Project(models.Model):
    prjname = models.CharField(max_length=128)

    def __unicode__(self):
        return self.prjname

class WorkLog(models.Model):
    user = models.ForeignKey(User)
    datefield = models.DateField()
    workhour = models.FloatField()
    project = models.ForeignKey(Project)
    content = models.TextField()

    def __unicode__(self):
        return str(self.datefield) + "【" + str(self.workhour) + "】 小时 - 项目:" + str(self.prj_name)

    @property
    def prj_name(self):
        return self.project.prjname

