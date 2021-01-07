from django.contrib import admin

from projects.models import Project, Hook


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class HookAdmin(admin.ModelAdmin):
    search_fields = ('project__name', 'created_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Hook, HookAdmin)
