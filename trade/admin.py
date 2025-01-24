from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MasterItem)
admin.site.register(InlineItem)
admin.site.register(UserRequestAllocation)
admin.site.register(AuthThreads)
