from django.contrib import admin
from .models import Company, Language, Programmer, Todo
# Register your models here.
admin.site.register(Company)
admin.site.register(Language)
admin.site.register(Programmer)
admin.site.register(Todo)