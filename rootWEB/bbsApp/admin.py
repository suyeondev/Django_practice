from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BbsUser)
admin.site.register(Bbs)
admin.site.register(Timeline)
admin.site.register(CsvToModel)