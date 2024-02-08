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
                "from": "HelpApp <hello@helpappafrica.com>",
                "to": email,
                "subject": "You're on the waitlist",
                "html": f"""
                    <!DOCTYPE html>
                    <html lang="en">
                   
                    <body>
                        <div class="container">
                            <td align="center" valign="top" bgcolor="#ffffff" style="border-radius:5px;border-left:1px solid #e0bce7;border-top:1px solid #e0bce7;border-right:1px solid #efefef;border-bottom:1px solid #efefef">
        <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">
          <tbody>
            <tr>
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;line-height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px; border-radius: 5px;">
              <img src="https://helpappafrica.com/static/images/help-img-345-werier34r3-32-removebg-preview.png"/>
                </td>
            </tr>
            
            <tr>
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;line-height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px">
              
                You're on the <span class="il">waitlist</span>!</td>
            </tr>
            

            
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
                Congratulations, thank you for joining the <span class="il">list</span> of potential help app users!. We will keep you updated on our launch date ,  feature roll outs and many more updates that you will be interested in</td>
            </tr>
            


            
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:20px 40px 20px 40px">
                Want to partner with us? Contact <span class="il">waiting</span>, us at <a href="tel:+16142161159" style="color: #9c28b1; text-decoration: none; font-weight: 600;">+1 (614) 216-1159</a> <span style="font-weight: 600;">Or</span> <a href="mailto:helpteam@helpaappafrica.com" style="color: #9c28b1;  text-decoration: none; font-weight: 600;">HelpTeam@helpaappafrica.com</a> </td>
            </tr>
            
            <tr>
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;line-height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px">
              <img src="https://helpappafrica.com/static/images/help-img-345-werier34r3-32.jpg"/>
                </td>
            </tr>
            
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:20px 20px 0px 40px">
                Thanks for registering!</td>
            </tr>
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:10px 40px 40px 40px">
                Help App team</td>
            </tr>
            
          </tbody>
        </table>
      </td>
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