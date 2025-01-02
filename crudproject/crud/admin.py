from django.contrib import admin

from crud.models import Students

class crudadmin(admin.ModelAdmin):
	list_display=('id','name','lname','email','age','image')
admin.site.register(Students,crudadmin)
