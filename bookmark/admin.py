from django.contrib import admin
# 북마크 앱 모델에서 클래스 임포트
from bookmark.models import Bookmark

# 어드민 클래스에서 리스트 출력 필드 항목을 지정
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

# 모델은 Bookmark, 어드민 클래스는 BookmarkAdmin으로 지정하여
# 어드민 사이트에 등록
admin.site.register(Bookmark, BookmarkAdmin)
