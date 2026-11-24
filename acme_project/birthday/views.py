from django.shortcuts import render
from .forms import BirthdayForm


def birthday(request):
    form = BirthdayForm()
    template = 'birthday/birthday.html'
    context = {
        'form': form
    }
    return render(request, template, context)
