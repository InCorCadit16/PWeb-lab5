from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Record
from .forms import RecordForm




def index(request):
    records = Record.objects.order_by('-pub_date')
    return render(request, 'index.html', {'records': records})


def news(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    return render(request, 'record.html', {'record': record})


@login_required
def my_records(request):
    records = Record.objects.filter(author=request.user).order_by('-pub_date')
    print(request.path)
    return render(request, 'index.html', {'records': records})


@login_required
def create_record(request):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'create_record.html', {'form': form, 'title': 'New Article'})
    else:
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.author = request.user
            record.pub_date = timezone.now()
            record.save()
            return redirect(f'/news/{record.id}')


@login_required
def edit_record(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'GET':
        form = RecordForm(instance=record)
        return render(request, 'create_record.html', {'form': form, 'title': 'Edit Article', 'id': record_id})
    else:
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record.save()
            return redirect(f'/news/{record.id}')


@login_required
def delete_record(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    if request.method == 'GET':
        return render(request, 'delete_record.html', {'record': record})
    else:
        record.delete()
        return redirect('/news/')
