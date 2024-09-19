from django import forms
from .models import Member

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'register_number', 'email', 'phone', 'department', 'year', 'community', 'prteam']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of the Participant'}),
            'register_number': forms.TextInput(attrs={'placeholder': 'Register Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'community': forms.Select(attrs={'class': 'form-control'}),
            'prteam': forms.Select(attrs={'class': 'form-control'}),
        }
