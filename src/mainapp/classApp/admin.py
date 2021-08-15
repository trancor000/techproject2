from django.contrib import admin

# Register your models here.
from .models import djangoClasses
from .models import djangoSchool
from .models import djangoAid
from .models import djangoGraduation


admin.site.register(djangoClasses)
admin.site.register(djangoSchool)
admin.site.register(djangoAid)
admin.site.register(djangoGraduation)