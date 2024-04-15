from django.contrib import admin
from indexapp.models import Products, Sections, Contacts, Categories

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    fields = ('name', 'description', 'application', 'image', 'sections', 'slug', 'category', )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Sections)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section',)
    fields = ('section',)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', 'description', )



@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', 'description', 'phone', 'adress', 'image',)

