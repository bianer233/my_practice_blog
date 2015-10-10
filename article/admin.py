from django.contrib import admin

# Register your models here.
from article.models import Article

# add for tinymc
# import models  
# Register your models here.

# class BlogAdmin(admin.ModelAdmin):  
#     class Media:  
#         js = (  
#             '/media/js/tiny_mce/tiny_mce.js',  
#             '/media/js/textareas.js',  
#         )  
admin.site.register(Article)