from django.contrib import admin
from .models import Qbank
from .models import Question

# Register your models here.
admin.site.register(Qbank)

admin.site.register(Question)
