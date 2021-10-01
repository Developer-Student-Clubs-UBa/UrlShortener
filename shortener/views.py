from django.shortcuts import render
from django.views.generic import DetailView

# Here goes the views
from shortener.utis import create_random_code


def home(request):  # Function base view
    context = {

    }
    return render(request, 'index.html', context)


class FirstView(DetailView):
    template_name = 'class_index.html'


def create_shortened_url(model_instance):
    random_code = create_random_code()
    # Gets the model class

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code
