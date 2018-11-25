from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

# 뷰 정의에서 템플릿 파일명을 지정하는 것이 일반적이지만,
# 여기서는 생략했으므로, 디폴트 템플릿명이 적욛됨.
# 디폴트 템플릿명은 모델명과 상속받는 제넥릭 뷰에 따라서 결정되는데,
# AlbumLV, AlbumDV, PhotoDV 뷰에 대한 디폴트 템플릿명은
# album_list.html, album_detail.html, photo_detail.html

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo
