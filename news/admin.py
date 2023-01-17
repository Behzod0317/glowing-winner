from django.contrib import admin

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at','updated_at']
    list_filter = ('created_at',)
    search_fields = ('name','id',)


    def text1(self,obj):
        return obj.text[:20+"..."]

admin.site.register(News,NewsAdmin)
