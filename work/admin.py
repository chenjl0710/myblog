# -*- coding: utf-8 -*-
from django.contrib import admin
import datetime
import time

# Register your models here.
from work.models import log, Project,weekReport,monthReport
from django.contrib.auth.admin import User
# https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#the-register-decorator

# Register your models here.
#https://www.cnblogs.com/wumingxiaoyao/p/6928297.html
@admin.register(log)
class LogAdmin(admin.ModelAdmin):
    # 添加Media是为了将textField的数入框变成富文本编辑框,
    #需要在textarea.js文件里添加对应的函数
    class Media:
        css = {'all':(
            'work/css/simditor.css',
        )}
        js = (
            # 'work/js/simditor/jquery.min.js',
            'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
            'work/js/simditor/module.js',
            'work/js/simditor/uploader.js',
            'work/js/simditor/hotkeys.js',
            'work/js/simditor/simditor.js',
            'work/js/rich_text.js',
            'work/js/textarea.js'
        )
    def get_queryset(self, request):
        #根据用户的权限，在列表里列出用户权限范围内的数据
        qs = super(LogAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user = User.objects.filter(username=request.user))

    def save_model(self, request, obj, form, change):
        #在保存时默认user的值是当前登录的用户
        obj.user = request.user
        super(LogAdmin,self).save_model(request, obj, form, change)


    fields = ('date','hour','project','content')#显示需要编辑的字段
    list_display = ('user','date','hour','project','content')  #在显示列表里显示字段
    list_filter = ('date','user','project')  #右侧的过滤器
    ordering = ('-date',)  #默认排序字段
    date_hierarchy = "date"   # 详细时间分层筛选　

    actions_on_top = False   #将顶部的动作action功能关闭

    # search_fields = ('user', 'project')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # 添加Media是为了将textField的数入框变成富文本编辑框
    class Media:
        css = {'all':(
            'work/css/simditor.css',
        )}
        js = (
            # 'work/js/simditor/jquery.min.js',
            'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
            'work/js/simditor/module.js',
            'work/js/simditor/uploader.js',
            'work/js/simditor/hotkeys.js',
            'work/js/simditor/simditor.js',
            'work/js/rich_text.js',
            'work/js/textarea.js'
        )

    list_display = ('projectname', 'remarks')

@admin.register(weekReport)
class weekReportAdmin(admin.ModelAdmin):
    # 添加Media是为了将textField的数入框变成富文本编辑框
    class Media:
        css = {'all':(
            'work/css/simditor.css',
        )}
        js = (
            # 'work/js/simditor/jquery.min.js',
            'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
            'work/js/simditor/module.js',
            'work/js/simditor/uploader.js',
            'work/js/simditor/hotkeys.js',
            'work/js/simditor/simditor.js',
            'work/js/rich_text.js',
            'work/js/textarea.js'
        )

    def getfirstday(self,weekflag):
        # weekflag格式为201435（即2014年第35周）
        #根据当前日期计算当前周的周日日期
        yearnum = weekflag[0:4]  # 取到年份
        weeknum = weekflag[4:6]  # 取到周
        stryearstart = yearnum + '0101'  # 当年第一天
        yearstart = datetime.datetime.strptime(stryearstart, '%Y%m%d')  # 格式化为日期格式
        yearstartcalendarmsg = yearstart.isocalendar()  # 当年第一天的周信息
        yearstartweek = yearstartcalendarmsg[1]
        yearstartweekday = yearstartcalendarmsg[2]
        yearstartyear = yearstartcalendarmsg[0]
        if yearstartyear < int(yearnum):
            daydelat = (8 - int(yearstartweekday)) + (int(weeknum) - 1) * 7
        else:
            daydelat = (8 - int(yearstartweekday)) + (int(weeknum) - 2) * 7
        a = (yearstart + datetime.timedelta(days=daydelat)).date()
        return a

    def save_model(self, request, obj, form, change):
        #在保存时默认user的值是当前登录的用户
        obj.user = request.user
        day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        week = datetime.datetime.strptime(day, "%Y-%m-%d").strftime("%W")
        obj.weekNum = day.split("-")[0] + u" 第" + week + u"周"
        monday = self.getfirstday(day.split("-")[0]+week)
        friday = monday + datetime.timedelta(days = 4)
        obj.weekCycle = str(monday) + "---" + str(friday) + u"周报"
        super(weekReportAdmin,self).save_model(request, obj, form, change)

    fields = ("lastWeekContent","thisWeekContent","nextWeekContent")#显示需要编辑的字段
    list_display = ('user','weekNum','weekCycle')  #在显示列表里显示字段
    list_filter = ('user','weekNum','weekCycle')  #右侧的过滤器
    ordering = ('-weekCycle',)  #默认排序字段
    # date_hierarchy = "weekCycle"   # 详细时间分层筛选　

    actions_on_top = False   #将顶部的动作action功能关闭

@admin.register(monthReport)
class monthReportAdmin(admin.ModelAdmin):
    # 添加Media是为了将textField的数入框变成富文本编辑框
    class Media:
        css = {'all':(
            'work/css/simditor.css',
        )}
        js = (
            # 'work/js/simditor/jquery.min.js',
            'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
            'work/js/simditor/module.js',
            'work/js/simditor/uploader.js',
            'work/js/simditor/hotkeys.js',
            'work/js/simditor/simditor.js',
            'work/js/rich_text.js',
            'work/js/textarea.js'
        )
    list_display = ("monthNum",)

# admin.site.register(log, admin_class=LogAdmin)
# admin.site.register(Project,ProjectAdmin)



#### 对应上面的export_as_json函数
# admin.site.add_action(export_as_json, "export_as_json")
####


admin.site.site_header = "数据运维组工作日志管理"
admin.site.site_title  = "工作日志系统"