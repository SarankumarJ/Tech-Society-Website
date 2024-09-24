from django.shortcuts import render, redirect
from .models import Community,leaders
from .forms import MemberRegistrationForm
from django.contrib import messages

# Home view for listing communities
def home(request):
    communities = Community.objects.all()  # Fetch all communities from the database
    return render(request, '../templates/home.html', {'communities': communities})

def register_member(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new member to the database
            messages.success(request, "Registration successful!")  # Success message
            # Re-render the same form with success message
            form = MemberRegistrationForm()  # Reset the form after success
            return render(request, '../templates/register_member.html', {'form': form})
        else:
            # Loop through the form errors and show them in the messages
            for field, error_messages in form.errors.items():
                for error in error_messages:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = MemberRegistrationForm()

    return render(request, '../templates/register_member.html', {'form': form})

from collections import defaultdict

def about(request):
    # Fetch all leaders ordered by their roles
    leaderships = leaders.objects.select_related('role').order_by('role__order')
    
    # Group leaders by their roles
    role_hierarchy = defaultdict(list)
    for leader in leaderships:
        role_hierarchy[leader.role].append(leader)

    return render(request, 'about.html', {'role_hierarchy': role_hierarchy})



