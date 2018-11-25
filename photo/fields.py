# 장고 기본 제공 필드인 ImageField, ImageFieldFile 임포트
from django.db.models.fields.files import ImageField, ImageFieldFile
# 파이썬 이미지 처리 라이브러리 PIL.Image 임포트
from PIL import Image
# 업로드된 파일을 서버에 저장하기 위해서 운영체제 라이브러리를 임포트
import os


# 지정한 이미지 파일에 대한 썸네일 이미지 파일명을 생성
def _add_thumb(s):              # 매개변수 s에는 파일 path가 전달됨
	parts = s.split(".")        # 문자열 나누기 https://wikidocs.net/13
	parts.insert(-1, "thumb")   # 마지막 원소 위치 앞에 삽입
	if parts[-1].lower() not in ['jpeg', 'jpg']:    # 확장자에 대한 검사
		parts[-1] = 'jpg'       # 확장자를 수정
	return ".".join(parts)      # "myPic.thumb.jpg"


class ThumbnailImageFieldFile(ImageFieldFile):
	# 필드 클래스에 상응하는 파일 처리 클래스
	# 파일 시스템에 직접 이미지 파일을 쓰고 지우는 작업 수행
	# https://www.programiz.com/python-programming/property
	# 파일의 경로와 URL 속성을 함께 제공해야 함
	def _get_thumb_path(self):
		return _add_thumb(self.path)    # self.path는 이미지 파일의 경로
	thumb_path = property(_get_thumb_path)

	def _get_thumb_url(self):
		return _add_thumb(self.url)     # self.url은 이미지 파일의 URL
	thumb_url = property(_get_thumb_url)

	def save(self, name, content, save=True):   # 파일 시스템에 파일을 저장하는 메소드
		super().save(name, content, save)   # 원본 이미지 파일 저장
		img = Image.open(self.path)
		size = (128, 128)
		img.thumbnail(size, Image.ANTIALIAS)    # PIL.Image.thumbnail() 함수로 썸네일 생성
		background = Image.new('RGBA', size, (255, 255, 255, 0)) # 흰색, 불푸명 배경 생성
		# 썸네일과 배경을 합성, 남는 여백은 배경에 의해 흰색이 됨
		background.paste(
			img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
		background.save(self.thumb_path, 'JPEG') # 합성된 최종 썸네일을 저장

	def delete(self, save=True): # 원본과 쎰네일 이미지를 모두 삭제
		if os.path.exists(self.thumb_path):
			os.remove(self.thumb_path)
		super().delete(save)


class ThumbnailImageField(ImageField): # 이 클래스가 모델 정의에 사용되는 필드
	# 새로운 필드 클래스 정의 시, 상응하는 파일 처리 클래스를 attr_class에 지정
	attr_class = ThumbnailImageFieldFile

	def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
		self.thumb_width = thumb_width      # 썸 네일 가로의 기본값은 128px
		self.thumb_height = thumb_height    # 썸 네일 세로의 기본값은 128px
		super().__init__(*args, **kwargs)
