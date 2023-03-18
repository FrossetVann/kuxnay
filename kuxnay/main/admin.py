from django.contrib import admin
from .models import Recipes
from .models import Tags
from .models import Structure
from .models import IpModel

admin.site.register(Recipes)
admin.site.register(Tags)
admin.site.register(Structure)
admin.site.register(IpModel)