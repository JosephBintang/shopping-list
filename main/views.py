from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Joseph Bintang ARdhirespati',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)