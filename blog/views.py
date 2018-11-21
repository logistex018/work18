# 뷰 작성에 필요한 클래스형 제넥릭 뷰 임포트
from django.views.generic import ListView, DetailView, TemplateView # ch07추가01 TemplateView
# 뷰 작성에 필요한 날짜 제네릭 뷰 임포트
from django.views.generic.dates import ArchiveIndexView, \
    YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
# blog.models.Post 클래스 임포트
from blog.models import Post
from tagging.models import Tag, TaggedItem                          # ch07추가02
from tagging.views import TaggedObjectList                          # ch07추가03

# 아래 두 클래스 추가                                               # ch07추가04
# TemplateView 제네릭 뷰는 테이블 처리 없이 단순 템플릿 렌더링 처리만 담당하는 뷰
class TagTV(TemplateView) :
    template_name = 'tagging/tagging_cloud.html' # 태그 클라우드를 출력하는 템플릿

# TaggedObjectList는 ListView를 상속받는 뷰로서,
# tagging 패키지는 tagging 패키지의 views.py에 정의되어 있는데,
# 모델과 태그가 지정되면, 해당 태그가 지정된 모델의 객체 리스트를
# 지정된 템플릿에 전달하는 역할
class PostTOL(TaggedObjectList) :
    model = Post
    template_name = 'tagging/tagging_post_list.html'

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

# ch09추가 1/1 시작
from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q                  # 검색 기능에 필요한 클래스
from django.shortcuts import render             # 단축 함수 render()

# FormView를 상속받아 SearchFormView 작성
# FormView는 GET 요청인 경우 폼을 화면에 보여주고 사용자 입력을 대기함
# 사용자가 폼에 데이터 입력 후 제출하면 이는 POST 요청으로 접수되고
# 입력 데이터에 대한 유효성 검사를 실시하여 유효하면
# form_valid() 함수를 실행한 후 적절한 URL로 리다이렉트 처리함
class SearchFormView(FormView):
    form_class = PostSearchForm             # 폼으로 사용할 클래스를 지정
    template_name = 'blog/post_search.html' # 템플릿 지정

    # 입력 데이터에 대한 유효성 검사를 실시하여 유효하면 실행될 함수
    def form_valid(self, form) :
	    # POST 요청의 id가 'search_word'인 값을 추출하여 변수에 저장
        schWord = '%s' % self.request.POST['search_word']
        # 개별 검색 1/
        schTitle = '%s' % self.request.POST['search_title']
        schDescription = '%s' % self.request.POST['search_description']
        schContent = '%s' % self.request.POST['search_content']
        schTag = '%s' % self.request.POST['search_tag']
        # filter() 메소드의 매칭 조건을 Q 객체로 다양하게 지정 가능함
	    # 각 조건에서 icontains 연산자는 대소문자 구별 없이
	    # 검색어가 포함되었는지 검사
	    # distinct() 메소드는 중복된 객체를 제외함
	    # 결국, Post 테이블의 모든 레코드에 대하여
	    # title, description, content, tag 필드에
	    # schWord가 포함된 레코드를 대소문자 구별 없이 검색해서 중복 없는 리스트로 저장
        post_list = Post.objects.filter(
	        Q(title__icontains=schWord) |
	        Q(description__icontains=schWord) |
	        Q(content__icontains=schWord) |
	        Q(tag__icontains=schWord)
        ).distinct()
        # 개별 검색 2/
        my_post_list = []

        if schTitle :
            my_post_list += Post.objects.filter(
                Q(title__icontains=schTitle)
            ).distinct()

        if schDescription :
            my_post_list += Post.objects.filter(
                Q(description__icontains=schDescription)
            ).distinct()

        if schContent :
            my_post_list += Post.objects.filter(
                Q(content__icontains=schContent)
            ).distinct()

        if schTag :
            my_post_list += Post.objects.filter(
                Q(tag__icontains=schTag)
            ).distinct()

        # 템플릿에 전달할 맥락 변수 context를 사전 형식으로 정의
        context = {}
        context['form'] = form  # 여기서 form은 PostSearchForm을 지칭함
        context['search_term'] = schWord
        context['object_list'] = post_list
        # 개별 검색 3/
        context['search_title'] = schTitle
        context['search_description'] = schDescription
        context['search_content'] = schContent
        context['search_tag'] = schTag
        context['my_object_list'] = my_post_list
		# 단축 함수 render()는 템플릿과 맥락 변수를 처리하여,
	    # 최종적으로 HttpResponse 객체를 반환
	    # 일반적으로 form_valid() 함수는 리다이렉트 처리를 위하여
	    # HttpResponseRedirect 객체를 반환하는데,
	    # 여기서는 render() 함수가 HttpResponse 객체를 반환하므로
	    # 리다이렉트 처리가 되지 않게됨.

        # form = PostSearchForm()
        return render(self.request, self.template_name, context)
# ch09 추가 1/1 종료
