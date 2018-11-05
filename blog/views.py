# 뷰 작성에 필요한 클래스형 제넥릭 뷰 임포트
from django.views.generic import ListView, DetailView
# 뷰 작성에 필요한 날짜 제네릭 뷰 임포트
from django.views.generic.dates import ArchiveIndexView, \
    YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
# blog.models.Post 클래스 임포트
from blog.models import Post

# ListView를 상속받아서 PostLV 작성
class PostLV(ListView) :
    model = Post
    # 기본값 'blog/post_list.html' 대신 지정 (3.1.4 URL 설계 항 참고)
    template_name = 'blog/post_all.html'
    # 컨텍스트 객체 이름을 기본값(object_list)와 다르게 지정했지만,
    # 기본값(object_list)도 여전히 사용 가능함
    context_object_name = 'posts'
    paginate_by = 5  # 페이지 당 5 개 객체를 처리하도록 지정

# DetailView를 상속받아서 PostDV 작성
# 기본키 대신 slug를 전달 받고, 나머지 속성은 기본값 사용
# slug는 URLconf가 전달해줌(3.1.4 URL 설계 항 참고)
class PostDV(DetailView) :
    model = Post

# 모든 아카이브 클래스에서 기준 날짜(date_filed) 속성을 modify_date로 지정

# ArchiveIndexView를 상속받아서 PostAV 작성
class PostAV(ArchiveIndexView) :
    model = Post
    date_field = 'modify_date'

# YearArchiveView를 상속받아서 PostYAV 작성
class PostYAV(YearArchiveView) :
    model = Post
    date_field = 'modify_date'
    make_object_list = True    # 기본값은 False이지만,
    # object_list 컨텍스트 변수를 생성해서 템플릿에 전달하도록 지시
    # URLconf에서 추출한 연도 값을 전달받아서 object_list를 구성하고
    # 이를 템플릿에 전달함

# MonthArchiveView를 상속받아서 PostMAV 작성
class PostMAV(MonthArchiveView) :
    model = Post
    date_field = 'modify_date'
    # URLconf에서 추출한 연도 및 월 값을 전달받아서 object_list를 구성하고
    # 이를 템플릿에 전달함

# DayArchiveView를 상속받아서 PostDAV 작성
class PostDAV(DayArchiveView) :
    model = Post
    date_field = 'modify_date'
    # URLconf에서 추출한 연도, 월, 일 값을 전달받아서 object_list를 구성하고
    # 이를 템플릿에 전달함

# TodayArchiveView를 상속받아서 PostTAV 작성
class PostTAV(TodayArchiveView) :
    model = Post
    date_field = 'modify_date'
    # URLconf에서 지정한 당일(today)에 해당하는 object_list를 구성하고
    # 이를 템플릿에 전달함

