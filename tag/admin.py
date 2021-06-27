from django.db.models.fields import CharField
from django.forms.widgets import Textarea, TextInput
from tag.models import QASample
from django.contrib import admin, messages
from tag.models import QASample, Answer
from django.db import models

admin.site.enable_nav_sidebar = False
admin.site.site_header = 'Gán nhãn dữ liệu hỏi đáp covid-19'
# Register your models here.

class AnswersInLine(admin.TabularInline):
    model = Answer
    extra = 0
    
class QASampleAdmin(admin.ModelAdmin):
    list_display = ('link', 'id', 'positive', 'question', 'hard_negative', 'answers')
    inlines = [AnswersInLine]
    list_per_page = 50
    access_range = {
        'phanuyen': (370, 469),
        'dangtienmanh': (770, 869),
        'thaotagging': (370, 469),
        'lantagging': (1320, 1519),
        'hanhtagging': (1220, 1319),
        'lexuanthuy': (270, 369),
        'levudoanh': (169, 269),
        'nguyenphuongthao': (370, 469),
        'phamthuyanh': (470, 569),
        'levudoanh': (870, 969),
        'danglamsan': (970, 1069),
        'thaotagging': (1070, 1169),
        'minhtagging': (770, 869),
    }

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'style': 'width: 80%',
                'rows': 20
            })
        },
        models.CharField: {
            'widget': TextInput(attrs={'style': 'width: 80%'})
        }
    }

    fieldsets = (
        ('POSITIVE', {
            'fields': ('positive_document_title', 'positive_document')
        }),
        ('QUESTION', {
            'fields': ('question',)
        }),
        ('HARD NEGATIVE', {
            'fields': ('hard_negative_document_title', 'hard_negative_document'),
        }),
    )

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        access_range = dict.get(QASampleAdmin.access_range, request.user.username, None)
        if access_range is None:
            return qs
        else:
            return qs.filter(id__range=access_range)
    
admin.site.register(QASample, QASampleAdmin)