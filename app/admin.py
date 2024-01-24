from django.contrib import admin
from .models import *


# Register your models here:

# register categroy in admen
admin.site.register(Category)

# register post app in admen
admin.site.register(Post)

# regester post comment in admen 
admin.site.register(PostComment)
