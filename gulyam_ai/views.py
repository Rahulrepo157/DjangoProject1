from django.shortcuts import render


def home(request):
    """View for the home page."""
    return render(request, 'home.html')


def careers(request):
    """View for the careers page."""
    return render(request, 'careers.html')


def thermosolver(request):
    return render(request, 'thermosolver.html')


def stressmaster(request):
    return render(request, 'stress master.html')


def about_us(request):
    """View for the about us page."""
    return render(request, 'about_us.html')


def product(request):
    return render(request, 'product.html')


def mechai(request):
    return render(request,'mech-ai.html')

def fluid_flow(request):
    return render(request,'fluid_flow_ai.html')

def design_master(request):
    return render(request,'design_master.html')

def manufactring_twin(request):
    return render(request,'manufactaring_ai.html')

def robopilot_ai(request):
    return render(request,'robopilot_ai.html')

def mat_si(request):
    return render(request,'mat_si.html')

