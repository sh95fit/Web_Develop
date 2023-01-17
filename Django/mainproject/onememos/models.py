from django.db import models

# Create your models here.
'''
간단 모델링
idx : 정수형
memo_text : 본문(문자열)
published_date : 날짜(date)
'''

# 클래스 작성 == 테이블 작성
class Memo(models.Model) :
    # 테이블의 각각의 필드가 된다!
    # id는 명시해주지 않으면 자동생성!
    memo_text = models.CharField(max_length=200)  # 글자 수 제한이 필요한 경우 CharField, 글자 수 제한이 없는 경우 TextField 사용
    published_date = models.DateTimeField(auto_now_add=True)    # 자동으로 현재 시각 입력