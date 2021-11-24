from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone

from .forms import NoticeForm
from .models import Notice


def index(request):
    notices = Notice.objects.all()
    notices.filter(pub_start__lte=timezone.now())
    notices.filter(pub_start__gte=timezone.now())
    context = { "notices": notices }
    return render(request, 'posts/index.html', context)

def new(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            newNotice = Notice(notice_title=form.cleaned_data['title'],
                               notice_text=form.cleaned_data['text'],
                               pub_start = form.cleaned_data['start'],
                               pub_end = form.cleaned_data['end'])
            newNotice.save()
            return redirect('index')
    context = {'form': NoticeForm()}
    return render(request, 'posts/edit.html', context)


def delete(request):
    notices = Notice.objects.all()
    notices.filter()