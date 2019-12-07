
from django.urls import path, include

from . import views

from rest_framework import routers



router_books = routers.DefaultRouter()

router_books.register('books', views.BooksList)



router_other = routers.DefaultRouter()

router_other.register('other', views.OtherList)



router_search = routers.DefaultRouter()

router_search.register('search', views.SearchList)


router_thesis = routers.DefaultRouter()

router_thesis.register('thesis', views.ThesisList)




router_feedback = routers.DefaultRouter()

router_feedback.register('feed', views.FeedBackList)


router_user = routers.DefaultRouter()

router_user.register('user', views.UserList)



urlpatterns = [
path('', include(router_books.urls)) ,
path('', include(router_other.urls)) ,
path('', include(router_search.urls)) ,
path('', include(router_thesis.urls)) ,
path('',include(router_feedback.urls)),
path('',include(router_user.urls)),
]


