# 문자열 처리 방식이 상이한 파이썬 버전 2 및 3의 호환성을 위한 임포트
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
# url 패턴을 만들어주는 장고 내장 함수 reverse()를 위한 임포트
from django.core.urlresolvers import reverse

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    # 아래에서 관리자 화면의 레이블과 도움말은 모두 한글로 수정하였음(교과서에서는 대문자 영문이었음)
    # 한 줄로 입력되는 CharField
    title = models.CharField('제목', max_length=50)
    slug = models.SlugField('슬러그',  # 기본 길이 50, 인덱스가 기본 생성됨,
                                       # 제목에서 주요 단어를 하으픈으로 연결하여 생성
                            unique=True,  # unique 설정, 기본키 대용으로 사용 가능
                            allow_unicode=True,  # 한글 입력 가능하도록
                            help_text='제목에 대한 한 단어의 별명.')
    description = models.CharField('설명',
                                   max_length=100,
                                   blank=True,  # 블랭크 허용
                                   help_text='간략한 설명 문구.')
    content = models.TextField('내용')  # TextField이므로 여러 줄 입력 가능함
    create_date = models.DateTimeField('최초 생성 일시',
                                       auto_now_add=True)  # 최초 생성 일시를 자동 저장하도록
    modify_date = models.DateTimeField('최종 수정 일시',
                                       auto_now=True)  # 최종 수정 일시를 자동 저장하도록

    class Meta:  # 필드 속성 외에 필요한 파라미터를 Meta 내부 클래스로 정의
        verbose_name = '기사'              # 'post'
        verbose_name_plural = '기사 모음'  # 'posts'
        db_table  = 'my_posts'           # DB에 저장할 테이블 이름을 my_posts'라고 지정
                                         # 기본값(앱이름_모델클래스이름)은 'blog_post'
        ordering  = ('-modify_date',)  # 최종 수정 일시의 내림차순 정렬

    def __str__(self):
        return self.title  # 객체를 출력할 때 제목만 출력

    def get_absolute_url(self): # 이 메소드가 정의된 객체를 지칭하는 URL을 반환
        # 아래에서 'blog:post_detail'는 blog 앱 이름공간의 post_detail이란 의미
        # # Example: /post/django-example/
        # url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
        return reverse('blog:post_detail', args=(self.slug,))
    def get_previous_post(self):  # 3.2.5 항에서 템플릿 작성할 때 사용
        return self.get_previous_by_modify_date()

    def get_next_post(self):  # 3.2.5 항에서 템플릿 작성할 때 사용
        return self.get_next_by_modify_date()
