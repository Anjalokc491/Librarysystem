from django.contrib import admin
from .models import login, register, BookList, UsedBookList, community

# Register your models here.
admin.site.register(login)
admin.site.register(BookList)
admin.site.register(UsedBookList)
admin.site.register(community)
