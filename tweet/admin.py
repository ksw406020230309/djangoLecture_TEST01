

from django.contrib import admin
from .models import TweetModel

# Register your models here.
admin.site.register(TweetModel)  # 나의 TweetModel을 Admin에 추가 해 줍니다
