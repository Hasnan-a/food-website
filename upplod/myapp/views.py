from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import Image  # <-- M
from .models import Image



# Create your views here.



from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
def services(request):
    pics=Image.objects.all()
    return render(request,'services.html',{"pics":pics})


# myapp/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def order_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'})

        subject = f"New Order from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                email,
                ['hasnan05110@gmail.com'],  # ✅ Your Gmail (receiver)
                fail_silently=False,
            )
            return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
        except BadHeaderError:
            return JsonResponse({'status': 'error', 'message': 'Invalid header found.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})




@login_required(login_url='login')

def HomePage(request):
       pics = Image.objects.all()
       return render(request, 'home.html', {'pics': pics})




def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if any field is empty
        if not uname or not email or not pass1 or not pass2:
            messages.error(request, "Please fill in all fields.")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=uname, email=email, password=pass1)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')