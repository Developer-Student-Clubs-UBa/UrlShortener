from django.shortcuts import render

from django.views.generic import DetailView


# Here goes the views

def home(request):  # Function base view
    context = {

    }
    return render(request, 'index.html', context)


class FirstView(DetailView):
    template_name = 'class_index.html'
