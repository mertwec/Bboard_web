from django.contrib import admin
from bboard.models import Board, Rubrick


class BoardAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "price", "published", "rubric") # последовательность имен полей, которые должны выводиться
                                                              # в списке записей;
    
    list_display_links = ("title", "content",)  # последовательность имен полей, которые должны быть
                                                # преобразованы в гиперссылки, ведущие на страницу правки записи;
    
    search_fields = ("title", "content",)   # последовательность имен полей, по которым должна выпол­
                                            # няться фильтрация.


admin.site.register(Rubrick)
admin.site.register(Board, BoardAdmin)
