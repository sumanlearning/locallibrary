from django.contrib import admin
from django.db import models
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	# fields = ('first_name', 'last_name', ('date_of_birth','date'))
# # register admin class with thr associated model
admin.site.register(Author, AuthorAdmin)

# register the admin classes for book using the detector
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
# 	list_display = ('title', 'author')#, 'display_genre')
# 	# def display_genre(self):
# 	 	#return ','.join([genre.name for genre self.in genre.all()[:3]])
	# display_genre.short_description = 'Genre'

# register the admin classes for bookinstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status','due_back')
	fieldsets = (
		(None, {
			'fields':('book', 'imprint','id')
			}),
		('Availability', {
			'fields': ('status','due_back')
			})
		)

class BooksInstanceInline(admin.TabularInline):
	model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')#, 'display_genre')
	inlines = [BooksInstanceInline]

	# def display_genre(self):
	# 	return ','.join([genre.name for genre in self.genre.all()])
	# display_genre.short_description="Genre"
