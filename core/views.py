from django.shortcuts import render, redirect
from core.models import WaitlistEmail
from core.forms import WaitlistForm
from django.contrib import messages
from django.http import JsonResponse


def index(request):
    email_submitted = WaitlistEmail.objects.all().count() + 1250
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = WaitlistForm(request.POST or None)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': f"nothing"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = WaitlistForm()
        

    context = {'form': form, "emails":email_submitted}
    return render(request,"index.html", context)



def success(request):
    return render(request, "success.html")