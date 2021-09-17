
# Register your models here.
from django.contrib import admin
from members.models import Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=('id','username','email','full_name','phone','password','created_at')
admin.site.register(Users, UsersAdmin)