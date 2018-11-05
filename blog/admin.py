from django.contrib import admin
from blog.models import Post

# Register your models here.

# blog.models.Post 클래스를 관리자 사이트에서 보여주는 방식 정의
class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'modify_date') # 관리자 화면에 보여줄 필드 지정
    list_filter   = ('modify_date',)  # 필터 사이드바를 출력
    search_fields = ('title', 'content')  # 검색 박스 표시하되, 입력된 값을 여기서 검색하라고 지정
    prepopulated_fields = {'slug': ('title',)}  # 슬러그 필드가 제목 필드의 값으로 자동 작성되도록 지정

admin.site.register(Post, PostAdmin)  # Post 및 PostAdmin 클래스를 관지자 사이트에 등록
