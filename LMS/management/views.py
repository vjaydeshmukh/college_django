from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_dashboard'))

    f1 = loginForm()

    if request.method == 'POST':
        f1 = loginForm(data=request.POST)
        if f1.is_valid():
            username = f1.cleaned_data['username']
            password = f1.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('user_dashboard'))
            else:
                return render(request, 'login.html',
                              context={'loginF': f1, 'message': 'Username/Password is invalid!!!'})
    return render(request, 'login.html', context={'loginF': f1})


@login_required(login_url='user_login')
def dash(request):
    profile = students.objects.get(user=request.user)
    book = books.objects.all()
    borrow = borrowed.objects.filter(issedby__user=request.user)
    fine = 0
    for i in borrow:
        d = (datetime.now().date() - i.issuedate).days
        if d > 5:
            fine += (int(d) - 5) * 10
    return render(request, 'dashboard.html', context={'profile': profile, 'books': book, 'borrow': borrow, 'fine': str(fine)})


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect(reverse('user_login'))


@login_required(login_url='user_login')
def borrowit(request, b_id):
    book = books.objects.get(isbn=b_id)
    if book.quantity > 0:
        obj, created = borrowed.objects.get_or_create(book=book, issedby=students.objects.get(user=request.user))
        if created:
            book.quantity -= 1
            book.save(update_fields=['quantity', ])
            obj.save()
    return HttpResponseRedirect(reverse('user_dashboard'))


@login_required(login_url='user_login')
def returnit(request, b_id):
    book = books.objects.get(isbn=b_id)
    book.quantity += 1
    book.save(update_fields=['quantity'])
    issued = borrowed.objects.get(issedby=students.objects.get(user=request.user), book=book)
    issued.delete()
    return HttpResponseRedirect(reverse('user_dashboard'))
