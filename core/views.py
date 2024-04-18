from django.shortcuts import render, redirect
from core.models import WaitlistEmail, Blog
from core.forms import WaitlistForm, ContactForm
from django.contrib import messages
from django.http import JsonResponse
import threading
import resend
resend.api_key = "re_R9H9FwgA_8VLXb3yScp54m18yqD38Ax2i"
def send_email_async(email_data):
    # Send the email using the resend module
    resend.Emails.send(email_data)

def index(request):
    blogs = Blog.objects.all().order_by('-id')[:5]
    context = {
        "blogs":blogs,
    }
    return render(request, "index.html", context)



def waitlist(request):
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
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;line-height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px">
              <img src="https://helpappafrica.com/static/images/help-img-345-werier34r3-32.jpg" style="border-radius: 15px;" height="200"/>
                </td>
            </tr>
            
            <tr>
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px">
              
                You're on the <span class="il">waitlist</span>!</td>
            </tr>
            

            
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
              Welcome to the Help App <span class="il">wait-list! </span><br> We're so excited to have you onboard.</td>
            </tr>
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
              By joining the wait-list, you're on step closer to being able to use our app to get the help you need. We're still in beta development, but we're working hard to make the app available to everyone as soon as possible</td>
            </tr>


            
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:20px 40px 20px 40px">
                Thanks for your patience and for being one of our early <span  style="color: #9c28b1; font-weight: 600;">supporters</span> </td>
            </tr>
            
            
             <tr>
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;line-height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px; border-radius: 5px;">
              <img src="https://helpappafrica.com/static/images/help-img-345-werier34r3-32-removebg-preview.png" height="100"/>
                </td>
            </tr>
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:20px 20px 0px 40px">
                 For enquiries contact us at <a href="mailto:helpteam@helpaappafrica.com" style="color: #9c28b1;  text-decoration: none; font-weight: 600;">HelpTeam@helpaappafrica.com</a></td>
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
    return render(request,"waitlist.html", context)


def success(request):
    return render(request, "success.html")


def about(request):
    return render(request, "about.html")

from django.http import JsonResponse

def contact(request):
    if request.method == "POST" and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            full_name = form.cleaned_data.get("full_name")
            email_data = {
                "from": "HelpApp <hello@helpappafrica.com>",
                "to": email,
                "subject": "We have gotten your message",
                "html": f"""
                    <!DOCTYPE html>
                    <html lang="en">
                   
                    <body>
                        <div class="container">
                            <td align="center" valign="top" bgcolor="#ffffff" style="border-radius:5px;border-left:1px solid #e0bce7;border-top:1px solid #e0bce7;border-right:1px solid #efefef;border-bottom:1px solid #efefef">
        <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0">
          <tbody>
            <tr>
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;line-height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px">
              <img src="https://helpappafrica.com/static/images/help-logo-removebg-preview.webp" style="border-radius: 15px;" height="200"/>
                </td>
            </tr>
            
            <tr>
              <td valign="top" align="center" style="font-family:Google Sans,Roboto,Helvetica,Arial sans-serif;font-size:36px;font-weight:500;height:44px;color:#202124;padding:40px 40px 0px 40px;letter-spacing:-0.31px">
              
                Hello <span class="il">{full_name}</span>!</td>
            </tr>
            

            
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:40px 40px 20px 40px">
              We have received your <span class="il">message </span><br> We'll get back to you soon.</td>
            </tr>
            
            
            <tr>
              <td valign="top" align="left" style="font-family:Roboto,Helvetica,Arial sans-serif;font-size:14px;line-height:24px;color:#414347;padding:20px 20px 0px 40px">
                Thanks for reaching out to us</td>
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
            return JsonResponse({'success': True, 'message': "Message sent successfully"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        # Handle non-AJAX requests here
        form = ContactForm()
        context = {'form': form}
        return render(request, "contact.html", context)



def team(request):
    return render(request, "team.html")

def blog_detail(request, bid):
    blog_bid = bid
    blog = Blog.objects.get(bid=blog_bid)
    context = {
        "blog": blog,
    }
    return render(request, "blog-detail.html", context)


def error_400(request, exception):
    return render(request, 'errors/400.html')

def error_401(request, exception):
    return render(request, 'errors/401.html')

def error_403(request, exception):
    return render(request, 'errors/403.html')

def error_404(request, exception):
    return render(request, 'errors/404.html')

def error_405(request, exception):
    return render(request, 'errors/405.html')

def error_500(request):
    return render(request, 'errors/500.html')

def error_503(request):
    return render(request, 'errors/503.html')

def error_504(request):
    return render(request, 'errors/504.html')
