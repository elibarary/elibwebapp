from django.contrib import admin
from django.urls import path,include
from libapp import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    

    url(r'^$', views.Home, name='home'),
    url(r'^books/$', views.books, name='books'),
    url(r'^search/$', views.search, name='search'),
    url(r'^thesis/$', views.thesis, name='thesis'),
    url(r'^other/$', views.other, name='other'),
    url(r'^feeds/$', views.Feeds, name='feeds'),
    path('login/', views.login_user, name='login'),
    path('webinfo/', views.webinfo, name='webinfo'),
    path('newfeed/', views.FeedCreateView.as_view(), name='newfeed'),
    url(r'^logout', views.logout_user, name='logout'),
    path('ditail/<int:book_id>/', views.Book, name='book'),
    path('ditails/<int:search_id>/', views.Searchd, name='search'),
    path('ditailt/<int:thesis_id>/', views.Thesisd, name='thesis'),
    path('ditailo/<int:other_id>/', views.Otherd, name='others'),
    path('api/', include('libapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/token/refresh/', TokenRefreshView.as_view() ),
    url(r'^auth/', include('djoser.urls') ),
    url(r'^auth/', include('djoser.urls.authtoken') ),
    url(r'^auth/', include('djoser.urls.jwt') ),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
