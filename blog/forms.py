# ch09 1/1 추가 시작
# 장고에서는 폼도 클래스로 정의 가능
from django import forms

# django.forms.Form 클래스를 상속받아 폼을 작성
class PostSearchForm(forms.Form):
    # 폼을 정의하는 방법은 테이블의 모델 클래스를 정의하는 방법과 유사함
    # CharField는 TextInput 위젯으로 표현됨
    # TextInput 위젯 압페 label이 표시되고,
    # 변수 search_word는 입력 필드에 대한 id 역할
    search_word = forms.CharField(label='검색어')
# ch09 1/1 추가 종료

