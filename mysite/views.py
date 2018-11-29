from django.views.generic.base import TemplateView

#                                                   ch11 1/2
# 테이블 레코드를 생성하기 위한 폼을 보여주고,
# 폼 입력에 따라 테이블 레코드를 생성하는 편집용 제네릭 뷰
# cf: CreateView, UpdateView, DeleteView, FormView
from django.views.generic.edit import CreateView
# User 모델의 객체 생성 폼
from django.contrib.auth.forms import UserCreationForm
# reverse_lazy() 및 reverse() 함수는 URL 패턴명을 인자로 전달 받는데,
# URL 패턴명을 인식하려면 urls.py 모듈이 메모리에 적재되어야 하고,
# 이를 최대한 지연시키기 위하여 reverse()가 아닌 reverse_lazy()를 적용
from django.core.urlresolvers import reverse_lazy

# TemplateView 제네릭 뷰를 상속받아서 HomeView 클래스 작성
class HomeView(TemplateView):
	# TemplateView를 상속받을 때 template_name 클래스 변수 오버라이딩은 필수
    # 템플릿 파일의 이름을 지정하는데, 파일의 위치는 settings.TEMPLATES.DIRS 항목에서 정의함
    template_name = 'home.html'

# 계정 등록                                         ch11 2/2
class UserCreateView(CreateView):
	# /accounts/register/ URL을 처리하는 뷰
	# 아래와 같이 중요한 속성만 지정하면, 그에 따라서 폼을 템플릿에 보여주고,
	# 입력 오류 검사 후, 입력한 내용으로 사용자 레코드를 생성하고,
	# 성공하면, success_url로 리다이렉트 시킴
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
	# User 생성이 성공하면 success_url 요청을 처리하는 뷰
	template_name = 'registration/register_done.html'