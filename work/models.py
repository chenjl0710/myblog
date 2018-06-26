# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.admin import User
# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     pwd = models.

class Project(models.Model):
    projectname = models.CharField(max_length=128, verbose_name='项目名称')
    remarks = models.TextField(max_length=128,blank=True,verbose_name='备注')

    def __unicode__(self):
        return self.projectname

    class Meta:
        verbose_name_plural = "项目"


class log(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名')
    date = models.DateField(verbose_name='日期')
    hour = models.FloatField(verbose_name='工时')
    project = models.ForeignKey(Project,verbose_name='项目名称')
    content = models.TextField(max_length=2048,verbose_name='工作内容')

    def __unicode__(self):
        return self.project.projectname

    class Meta:
        verbose_name_plural = "工作日志"

class weekReport(models.Model):
    user = models.CharField(max_length=256,verbose_name="姓名")
    weekNum = models.CharField(max_length=256,verbose_name="周次")
    weekCycle = models.CharField(max_length=256,verbose_name="周报时间")
    lastWeekContent = models.TextField(max_length=10240,verbose_name="本周工作计划")
    thisWeekContent = models.TextField(max_length=10240,verbose_name="本周工作内容")
    nextWeekContent = models.TextField(max_length=10240,verbose_name="下周工作计划")

    def __unicode__(self):
        return self.weekCycle + "工作内筒"

    class Meta:
        verbose_name_plural = "周报"

class monthReport(models.Model):
    user = models.CharField(max_length=256, verbose_name="姓名")
    project = models.CharField(max_length=128, verbose_name='项目名称')
    monthNum = models.CharField(max_length=256,verbose_name="月份")
    monthCycle = models.CharField(max_length=256,verbose_name="月报时间")
    monthWorkHour = models.TextField(max_length=10240,verbose_name="月工时")

    def __unicode__(self):
        return self.monthNum + "月报"

    class Meta:
        verbose_name_plural = "月报"