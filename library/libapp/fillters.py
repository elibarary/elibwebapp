from .models import BooksModel
import django_filters

class BooksFilter(django_filters.FilterSet):




    class Meta:
        model = BooksModel
        fields = {

        'title':['contains'],


        }