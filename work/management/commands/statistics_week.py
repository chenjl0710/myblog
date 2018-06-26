from django.core.management.base import BaseCommand,CommandError
from work.models import weekReport
from django.contrib.auth.admin import User,Group

class Command(BaseCommand):
    help = "定时每周五中午12:00自动将上周中的下周计划和本周的工作日志里的工作内容写入本周工作内容 中。"

    def handle(self, *args, **options):
        for gp in options["group_id"]:
            try:
                gp_id = Group.objects.get(pk=gp)
                self.stdout.write('Successfully closed Group id "%s"' % gp_id)
            except Group.DoesNotExist:
                raise CommandError('Group "%s" does not exist' % gp)
