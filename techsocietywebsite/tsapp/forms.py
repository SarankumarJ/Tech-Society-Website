from django import forms
from .models import Member, Department, Year, Community, PRTeam

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'register_number', 'email', 'phone', 'department', 'year', 'community', 'prteam']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of the Student', 'class': 'form-control'}),
            'register_number': forms.TextInput(attrs={'placeholder': 'Register Number', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MemberRegistrationForm, self).__init__(*args, **kwargs)
        
        # Fetch choices from the database for 'department'
        self.fields['department'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=[('', 'Choose Department')] + [(dept.id, dept.name) for dept in Department.objects.all()]
        )
        
        # Fetch choices from the database for 'year'
        self.fields['year'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=[('', 'Choose Year')] + [(year.id, year.name) for year in Year.objects.all()]
        )
        
        # Fetch choices from the database for 'community'
        self.fields['community'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=[('', 'Choose Community')] + [(community.id, community.name) for community in Community.objects.all()]
        )
        
        # Fetch choices from the database for 'prteam'
        self.fields['prteam'].widget = forms.Select(
            attrs={'class': 'form-control'},
            choices=[('', 'Choose PR Team')] + [(prteam.id, prteam.name) for prteam in PRTeam.objects.all()]
        )
        
    # Unique registration number validation
    def clean_register_number(self):
        register_number = self.cleaned_data.get('register_number')
        if Member.objects.filter(register_number=register_number).exists():
            raise forms.ValidationError("This registration number is already in use.")
        return register_number

    # Phone number validation
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 10:
            raise forms.ValidationError("Enter a valid 10-digit phone number.")
        if not phone.isdigit():
            raise forms.ValidationError("Phone number should contain digits only.")
        return phone
