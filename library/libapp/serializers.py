from .models import BooksModel , FeedBack , ThesisModel , SearchModel , OtherModel
from rest_framework import  serializers
from django.contrib.auth.models import User

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BooksModel
        fields = ['id','call_No','title','author','speciality','file','date']


class OtherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OtherModel
        fields = ['id','call_No','title','author','speciality','file','date']

class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchModel
        fields = ['id','call_No','title','author','speciality','file','date']

class ThesisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThesisModel
        fields = ['id','call_No','title','author','speciality','file','date']



class FeedBackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['id','name','email','body']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','is_staff','is_superuser']







































