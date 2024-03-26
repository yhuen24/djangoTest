from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


# def user_login(request):
   # return render(request, 'registration/login.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Logic for successful login
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
