from django.shortcuts import render, redirect

# Add the following import
from django.http import HttpResponse

from .forms import WidgetForm
from .models import Widget

# Define the home view
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {
        "widget_form": widget_form,
        "widget_list": widgets,
    })

def create(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        add_widget = form.save(commit=False)
        add_widget.save()
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return redirect('/', {
        "widget_form": widget_form,
        "widget_list": widgets,
    })

def delete(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return redirect('/', {
        "widget_form": widget_form,
        "widget_list": widgets,
    })