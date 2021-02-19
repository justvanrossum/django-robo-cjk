# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from robocjk.models import Project


class Command(BaseCommand):

    help = 'Export all .rcjk projects and push changes to their own git repositories.'

    def handle(self, *args, **options):
        projects_qs = Project.objects.prefetch_related('fonts').filter(export_running=False)
        for project in projects_qs:
            project.export()
