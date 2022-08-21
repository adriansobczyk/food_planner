from django.contrib import admin

from .models import List, Task

admin.site.register(List)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_list', 'created')
    readonly_fields = list_display
admin.site.register(Task, TaskAdmin)