import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Community, Department, Year, PRTeam, Member

def export_as_csv(modeladmin, request, queryset):
    """ Export data as CSV """
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={opts.verbose_name_plural}.csv'
    writer = csv.writer(response)

    # Write the header
    fields = [field.name for field in opts.get_fields() if not field.many_to_one]
    writer.writerow(fields)

    # Write the data
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])

    return response

export_as_csv.short_description = 'Export selected items as CSV'


class CommunityAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

class DepartmentAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

class YearAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

class PRTeamAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

class MemberAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

admin.site.register(Community, CommunityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(PRTeam, PRTeamAdmin)
admin.site.register(Member, MemberAdmin)
