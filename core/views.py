from django.shortcuts import render, redirect
from core.models import WaitlistEmail
from core.forms import WaitlistForm
from django.contrib import messages
from django.http import JsonResponse
import threading
import resend
resend.api_key = "re_R9H9FwgA_8VLXb3yScp54m18yqD38Ax2i"
def send_email_async(email_data):
    # Send the email using the resend module
    resend.Emails.send(email_data)


def index(request):
    email_submitted = WaitlistEmail.objects.all().count() + 1250
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = WaitlistForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            
            # Define the email data
            email_data = {
                "from": "Help App <helpteam@helpappafrica.com>",
                "to": email,
                "subject": "Help App Africa waitlist",
                "html": f"""
                    <!DOCTYPE html>
                    <html lang="en">
                   
                    <body>
                        <div class="container">
                            <h1>Hey friend,<br></h1>
                            <p>Congratulations, thank you for joining the list of potential help app users!</p>
                            <p>we will keep you updated on our launch date, feature roll outs and many more updates that you will be interested in.</p><br><br><br>
                            <p>Want to partner with us ? </p><br>
                            <div style="text-align: left; align-items: left;">
                                <p>Contact us at <a href="tel:+16142161159">+1 (614) 216-1159</a> Or <a href="mailto:helpteam@helpaappafrica.com">HelpTeam@helpaappafrica.com</a></p><br><br>
                            </div>
                            <p style="font-size: 12px; text-align: center; align-items: center;">
                                Note: This email is sent as part of Help App Afica communication. If you believe this is a mistake or received this email in error, please disregard it.
                            </p>
                        </div>
                    </body>
                    </html>
                """,
            }

            # Create a thread to send the email asynchronously
            email_thread = threading.Thread(target=send_email_async, args=(email_data,))
            email_thread.start()
            
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