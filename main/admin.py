from django.contrib import admin
from main.models import Question, Choice, Bar_code, Img, Imgadd

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Bar_code)
admin.site.register(Img)
admin.site.register(Imgadd)