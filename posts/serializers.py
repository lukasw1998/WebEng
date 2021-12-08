from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Notice
            fields = ('id', 'notice_title', 'notice_text', 'pub_start', 'pub_end')