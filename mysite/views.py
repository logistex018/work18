from django.views.generic.base import TemplateView

# TemplateView 제네릭 뷰를 상속받아서 HomeView 클래스 작성
class HomeView(TemplateView):
	# TemplateView를 상속받을 때 template_name 클래스 변수 오버라이딩은 필수
	# 템플릿 파일의 이름을 지정하는데, 파일의 위치는 settings.TEMPLATES.DIRS 항목에서 정의함
	template_name = 'home.html'