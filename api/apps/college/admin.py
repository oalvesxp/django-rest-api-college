from django.contrib import admin
from apps.college.models import \
    Student, Course

class Students(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'rg',
        'cpf',
        'birth',
    )
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)
