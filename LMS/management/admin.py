from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


class bookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity')
    list_filter = ('author', )
    search_fields = ('isbn', 'title', 'author')


class studentAdmin(admin.ModelAdmin):
    list_filter = ('branch', 'year')
    search_fields = ('prn', )


class issueAdmin(admin.ModelAdmin):
    list_display = ('book', 'issuedate', 'issedby')
    list_filter = ('issuedate', 'book')
    search_fields = ('issedby', 'book')


admin.site.site_header = "Library Management System"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to Library Management System"
admin.site.register(students, studentAdmin)
admin.site.register(books, bookAdmin)
admin.site.register(borrowed, issueAdmin)
admin.site.unregister(Group)
