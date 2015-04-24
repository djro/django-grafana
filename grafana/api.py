from django.templatetags.static import static
from django.shortcuts import redirect


def home_dashboard(request):
    return redirect(static('json/home_dashboard.json'))