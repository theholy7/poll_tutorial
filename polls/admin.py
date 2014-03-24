from django.contrib import admin
from polls.models import Choice, Poll


# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]

admin.site.register(Poll, PollAdmin)
