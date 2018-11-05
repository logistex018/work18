from django.conf.urls import url
# from bookmark.views import BookmarkLV, BookmarkDV # 교과서 ch02 52쪽의 원래 코드를 아래와 같이 수정함
from . import views  # 이렇게 수정하면 아래 코드에서와 같이 views.~ 형식으로 변경해야 함
urlpatterns = [
    # ch02에서 코딩했던 부분을 아래와 같이 수정하였으므로 주석 처리함
    # # 북마크 앱을 위한 클래스 기반 뷰
    # # /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
    # # /bookmark/숫자/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),
    # # tabular list
    # url(r'^bookmark_t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
    # url(r'^bookmark_t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),

    # 북마크 앱을 위한 클래스 기반 뷰
    # /bookmark/ 요청을 처리할 뷰 클래스를 BookmarkLV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
    # ch02 코드는 위와 같았으나, 아래처럼 수정함
    # 왜냐하면, mysite.urls에서 '^bookmark/' 부분과 일치하는 request.path 부분이 처리되고,
    # 처리된 부분이 제거된 나머지 request.path 부분만 bookmark.urls로 전달되므로!!!
    url(r'^$', views.BookmarkLV.as_view(), name='index'),
    # /bookmark/숫자/ 요청을 처리할 뷰 클래스를 BookmarkDV로 지정하고, URL 패턴 이름 지정
    # url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),
    # tabular list
    # url(r'^bookmark_t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
    # url 패턴 매칭을 '/' 단위로 처리하기 위하여 아래와 같이 수정
    # 이에 따라서 템플릿에서도 수정이 필요함
    url(r'^t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
    # url(r'^bookmark_t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),
    # url 패턴 매칭을 '/' 단위로 처리하기 위하여 아래와 같이 수정
    # 이에 따라서 템플릿에서도 수정이 필요함
    url(r'^t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),
]
# 주의할 점
# bookmark.urls 내부에서 지정한 url 패턴의 이름 'index', 'detail', ... 등을
# 템플릿에서 사용할 때, 이름공간 bookmark를 포함하도록
# 'bookmark:index','bookmark:detail', ... 등으로 변경해주어야 함!!!
