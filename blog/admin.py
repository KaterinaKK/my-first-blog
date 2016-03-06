from django.contrib import admin
from .models import Post
print('admin work!')

admin.site.register(Post)

