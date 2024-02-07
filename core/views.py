from django.shortcuts import render, redirect
from core.models import WaitlistEmail
from core.forms import WaitlistForm
from django.contrib import messages
from django.http import JsonResponse


def index(request):
    email_submitted = WaitlistEmail.objects.all().count
    if request.method == 'POST':
        form = WaitlistForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"You've been added to the waitlist")
            return redirect('core:success')
    else:
        form = WaitlistForm()

    context = {'form': form, "emails":email_submitted}
    return render(request,"index.html", context)



def success(request):
    return render(request, "success.html")