# resources.py
from import_export import resources
from .models import Community, Department, Year, PRTeam, Member

class CommunityResource(resources.ModelResource):
    class Meta:
        model = Community

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department

class YearResource(resources.ModelResource):
    class Meta:
        model = Year

class PRTeamResource(resources.ModelResource):
    class Meta:
        model = PRTeam

class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
