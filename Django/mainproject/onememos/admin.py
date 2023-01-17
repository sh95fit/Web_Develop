from django.contrib import admin
# 앱 추가
from onememos.models import Memo


# Register your models here.

# 어드민 사이트에 models.py에 적용한 클래스(테이블)을 반영해주기 위해 추가
admin.site.register(Memo)