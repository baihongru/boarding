from django.contrib import admin

from .models import Candidate

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('username', 'city', 'degree', 'first_score', 'first_result',
                    'first_interviewer', 'second_score', 'second_result',
                    'second_interviewer', 'third_score', 'third_result',
                    'third_interviewer', 'last_editor')
    readonly_fields = ('creator', 'created_date', 'modified_date')
    fieldsets = [
        (None, {
            'fields': [
                'userid',
                ('username', 'gender'),
                ('phone', 'email'),
                ('city', 'apply_position'),
                ('major', 'degree'),
                'bachelor_school',
                'master_school',
                'doctor_school',
                'born_address',
                ('comprehensive_score', 'paper_score'),
                'candidate_remark',
                'last_editor',
            ],
        }),
        ('初试记录', {
            'fields': [
                'first_interviewer',
                ('first_score_learning', 'first_score_professional'),
                ('first_score', 'first_result'),
                'first_recommend_position',
                'first_advantage',
                'first_disadvantage',
                'first_remark',
            ],
            #'classes': ['collapse'],
        }),
        ('专业能力面试记录', {
            'fields': [
                'second_interviewer',
                ('second_score_professional', 'second_score_learning'),
                ('second_score_communication', 'second_score_excellent'),
                'second_score_anti_pressure',
                ('second_score', 'second_result'),
                'second_recommend_position',
                'second_advantage',
                'second_disadvantage',
                'second_remark',
            ],
            #'classes': ['collapse'],
        }),
        ('HR终面记录', {
            'fields': [
                'third_interviewer',
                ('third_score_responsibility', 'third_score_communication', 'third_score_stability'),
                ('third_score_logic', 'third_score_potential'),
                ('third_score', 'third_result'),
                'third_advantage',
                'third_disadvantage',
                'third_remark',
            ],
            #'classes': ['collapse'],
        }),
        ('其他', {
            'fields': [
                ('creator', 'created_date', 'modified_date'),
            ],
            'classes': ['collapse'],
        })
    ]

    def save_model(self, request, obj, form, change):
        if not obj.creator:
            obj.creator = request.user.username
        obj.last_editor = request.user.username
        super().save_model(request, obj, form, change)

admin.site.register(Candidate, CandidateAdmin)
