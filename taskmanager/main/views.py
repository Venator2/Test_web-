from django.shortcuts import render
from .models import IdentificationUser
from .forms import UserForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        ls = IdentificationUser.objects.all()
        if form.is_valid():
            if len(ls) == 0:
                form.save()

            first = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            full = first + last
            list_of_names = [u.full_name for u in ls]
            if full in list_of_names:
                messages.success(request, 'Вже бачилися, ' + first + '.')
            else:
                messages.success(request, 'Привіт, ' + first + ' ' + last + '.')
                form.save()

    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)


def users(request):
    names = IdentificationUser.objects.all()
    return render(request, 'main/users.html', {'names': names})
