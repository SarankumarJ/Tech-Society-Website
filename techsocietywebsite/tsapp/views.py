from django.shortcuts import render, redirect
from .models import Community, Member
from .forms import MemberRegistrationForm
from django.contrib import messages

# Home view for listing communities
def home(request):
    communities = Community.objects.all()  # Fetch all communities from the database
    return render(request, '../templates/home.html', {'communities': communities})


from django.contrib import messages

def register_member(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new member to the database
            messages.success(request, "Registration successful!")  # Success message
            # Render the same template with the success message
            return render(request, '../templates/register_member.html', {'form': form})
        else:
            # If the form is not valid, check for errors
            for error in form.errors:
                if error == 'register_number':
                    messages.warning(request, form.errors[error][0])  # Show warning for registration number
    else:
        form = MemberRegistrationForm()
    
    return render(request, '../templates/register_member.html', {'form': form})


