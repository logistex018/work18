from django.conf.urls import include, url
from django.contrib import admin
# static() 함수는 정적 파일 처리하는 뷰를 호출할 수 있도록 URL 패턴을 반환
from django.conf.urls.static import static                              # ch10 1/4
# settings 변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 객체에 대한 참조
from django.conf import settings                                        # ch10 2/4

from mysite.views import HomeView
# 회원 가입 처리 뷰 임포트
from mysite.views import UserCreateView, UserCreateDoneTV               # ch11 1/2

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	# 아래 인증 관련 3행 추가                                           ch11 2/2
	# 장고 인증 URLconf를 인클루드하는데, 여기에 정의된 /login, /logout 등이
	# /accounts/login, /accounts/logout, /accounts/password_change/가 됨
	url(r'^accounts/', include('django.contrib.auth.urls')),
	# 계정 가입 처리하는 URL
	url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
	# 계정 가입 완료될 때 보여줄 URL
	url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

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
