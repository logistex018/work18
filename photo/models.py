from django.db import models
# reverse() 함수는 URL 패턴을 만들어주는 장고 내장 함수
from django.core.urlresolvers import reverse
# ThumbnailImageField 클래스는 사진 원본 및 썸네일 이미지를 저장하는
# (fields.py 파일에서 정의할) 커스텀 필드
from photo.fields import ThumbnailImageField
from pytz import timezone


class Album(models.Model):
	name = models.CharField('앨범 이름', max_length=50)
	description = models.CharField('앨범 설명', max_length=100, blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# 이 메소드가 정의된 객체의 URL /photo/album/99 형식의 값을 반환
		return reverse('photo:album_detail', args=(self.id,))

# from django.db.models import Q
# from django.core.exceptions import ObjectDoesNotExist

class Photo(models.Model):
	# 자신의 부모(Album)에 대한 외래키
	album = models.ForeignKey(Album)
	title = models.CharField('사진 제목', max_length=50)
	# ThumbnailImageField는 upload_to 옵션으로 저장 위치를 지정
	# MEDIA_ROOT로 지정된 폴더 하위에 /photo/2018/03/과 같은 폴더를 생성하고,
	# 여기에 업로드된 파일을 자동적으로 저장해줌
	image = ThumbnailImageField(upload_to='photo/%Y/%m')
	description = models.TextField('사진 설명', blank=True)
	# settings.TIME_ZONE = 'Asia/Seoul' 으로 설정해도 UTC 시각으로 처리됨
	# DB에 저장되는 시각은 UTC 시각이지만, 아래 속성 처리로 한국 시각으로 변환하여 템플릿에 제공함
	upload_date = models.DateTimeField('등록 일시', auto_now_add=True)

	# 아래와 같이 속성 처리를 변경해야 한국 시각으로 처리됨
	@property
	def created_at_korean_time(self):
		korean_timezone = timezone(settings.TIME_ZONE)
		return self.created_at.astimezone(korean_timezone)

	class Meta:
		ordering = ['-upload_date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# 이 메소드가 정의된 객체의 URL /photo/photo/99 형식의 값을 반환
		return reverse('photo:photo_detail', args=(self.id,))

	# ver#3.0 https://stackoverflow.com/questions/39947041/how-to-continue-the-object-in-django-get-next-previous-by-date-created-and-publi
	# filter 사용법: http://brownbears.tistory.com/63
	def get_newer_photo(self):  						# ch10_nav
		newer_photo = Photo.objects.filter(
			upload_date__gt = self.upload_date
			, album = self.album
		).order_by('upload_date').first()
		return newer_photo

	def get_older_photo(self):      					# ch10_nav
		older_photo = Photo.objects.filter(
			upload_date__lt = self.upload_date
			, album = self.album
		).order_by('-upload_date').first()
		return older_photo

	# # ver#1.0 이렇게 하면 앨범별로 구분되지 않고 이전/다음 처리가 됨
	# def get_previous_photo(self):  # ch10_nav
	# 	return self.get_previous_by_upload_date()
	#
	# def get_next_photo(self):  # ch10_nav
	# 	return self.get_next_by_upload_date()

	# # ver#2.0 이렇게 하면 앨범별로 구분은 되는데, 첫/끝 객체로 이동이 안되네!!!
	# def get_next_photo(self): 					# ch10_nav
	# 	while True:
	# 		next_photo = self.get_next_by_upload_date()
	# 		if next_photo.album == self.album:
	# 			break
	# 		# if not next_photo:
	# 		# 	break # return None
	# 		# elif next_photo.album == self.album:
	# 		# 	break
	# 		# else:
	# 		# 	pass # 다음 사진으로 이동
	# 	return next_photo
	#
	# def get_previous_photo(self):  						# ch10_nav
	# 	while True:
	# 		prev_photo = self.get_previous_by_upload_date()
	# 		if not prev_photo:
	# 			break #return None
	# 		elif prev_photo.album == self.album:
	# 			break
	# 		else:
	# 			pass # 이전 사진으로 이동
	# 	return prev_photo

	# # ver#2.5 이렇게 하면 앨범별로 구분은 되는데, 첫/끝 객체로 이동이 안되네!!!
	# def get_previous_photo(self): 					# ch10_nav
	# 	while True:
	# 		try:
	# 			prev_photo = self.get_previous_by_upload_date()
	# 			if not prev_photo:
	# 				return None
	# 			elif prev_photo and prev_photo.album == self.album:
	# 				break
	# 		except ObjectDoesNotExist:
	# 			return None
	# 	return prev_photo
	#
	# def get_next_photo(self):  						# ch10_nav
	# 	while True:
	# 		try:
	# 			next_photo = self.get_previous_by_upload_date()
	# 			if not next_photo:
	# 				return None
	# 			elif next_photo and next_photo.album == self.album:
	# 				break
	# 		except ObjectDoesNotExist:
	# 			return None
	# 	return next_photo
