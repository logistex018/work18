from django.db import models

# 장고에서
# 테이블은 (django.dbmodels.Model을 상속받는) 클래스로 정의하고,
# 테이블 컬럼은 클래스 변수로 정의함
class Bookmark(models.Model):
    # id 필드(Integer, PK, Auto Increment)는 자동 생성됨
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)   # 'url'은 Field.verbose_name(별칭)

    def __str__(self):  # 객체를 문자열로 출력할 때 사용하는 함수
        return self.title