from django.contrib import admin
from .models import BooksModel , FeedBack ,BestBooks , OtherModel , SearchModel , ThesisModel ,FileModel
from import_export.admin import ImportExportModelAdmin

admin.site.register(FeedBack)


admin.site.register(BestBooks)

@admin.register(FileModel)

class File(ImportExportModelAdmin):

    class Meta:
        model = FileModel



@admin.register(BooksModel)

class Book(ImportExportModelAdmin):

    class Meta:
        model = BooksModel



@admin.register(OtherModel)

class Message(ImportExportModelAdmin):

    class Meta:
        model = OtherModel



@admin.register(SearchModel)

class Search(ImportExportModelAdmin):

    class Meta:
        model = SearchModel


@admin.register(ThesisModel)

class Thesis(ImportExportModelAdmin):

    class Meta:
        model = ThesisModel














