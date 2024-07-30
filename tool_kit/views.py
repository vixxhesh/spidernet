from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tool_kit/tool_kit_home.html')