from django.contrib import admin
from tomatoDotCom.models import student, teacher, user, qna, notice, info


class tomatoAdmin_usr(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'pw', 'created_at', 'updated_at')

class tomatoAdmin_brd(admin.ModelAdmin):
    list_display = ('author', 'title', 'body', 'created_at', 'updated_at')

admin.site.register(student, tomatoAdmin_usr)
admin.site.register(teacher, tomatoAdmin_usr)
admin.site.register(user, tomatoAdmin_usr)
admin.site.register(qna, tomatoAdmin_brd)
admin.site.register(notice, tomatoAdmin_brd)
admin.site.register(info, tomatoAdmin_brd)