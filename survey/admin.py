from django.contrib import admin
from django.http import HttpResponseRedirect


from survey.models import Survey

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    readonly_fields=('published',)

    change_form_template = 'admin/survey/survey/change_form.html'

    def response_change(self, request, instance):
        if "_publish" in request.POST:
            instance.publish()
            instance.send_request()
            return HttpResponseRedirect(".")
        return super().response_change(request, instance)
