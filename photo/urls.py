from django.conf.urls import url
from photo.views import *

urlpatterns = [
    # Example: /
    url(r'^$', AlbumLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),

	# Example: /album/99/
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),

	# Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),

	# 아래처럼 정의하면 PhotoDV 뷰 정의를 생략하고
	# urlpatterns 정의만으로 일을 끝낼 수 있지만, MTV 원칙에는 맞지 않음
	# url(r'^$', ListView.as_view(model=Album), name='index'),
	# url(r'^album/$', ListView.as_view(model=Album), name='album_list'),
	# url(r'^album/(?P<pk>\d+)/$', DetailView.as_view(model=Album), name='album_detail'),
	# url(r'^photo/(?P<pk>\d+)/$', DetailView.as_view(model=Photo), name='photo_detail'),
]

