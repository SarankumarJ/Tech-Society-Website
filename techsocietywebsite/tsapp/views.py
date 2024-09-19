from django.shortcuts import render, redirect
from .models import Community, Member
from .forms import MemberRegistrationForm

# Home view for listing communities
def home(request):
    communities = Community.objects.all()  # Fetch all communities from the database
    return render(request, '../templates\home.html', {'communities': communities})

# View for member registration
def register_member(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new member to the database
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = MemberRegistrationForm()
    
    return render(request, '../templates/register_member.html', {'form': form})
