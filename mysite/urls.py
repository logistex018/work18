from django.conf.urls import include, url
from django.contrib import admin
# static() 함수는 정적 파일 처리하는 뷰를 호출할 수 있도록 URL 패턴을 반환
from django.conf.urls.static import static                              # ch10 1/4
# settings 변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 객체에 대한 참조
from django.conf import settings                                        # ch10 2/4

from mysite.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),          # ch10 3/4

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)     # ch10 4/4
# 기존 urlpatterns에 static() 함수가 반환하는 URL 패턴을 추가
# static(prefix, view=django.views.static.serve, **kwargs)
# settings.MEDIA_URL = '/media/' 이런 URL 요청이 오면,
# django.views.static.serve() 뷰 함수가 처리하게 되어 있는데,
# 이 뷰 함수에 다음 인자를 전달함
# document_root = settings.MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
