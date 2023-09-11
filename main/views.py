from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Muhamad Hanif Nurrifky Wicaksono',
        'amount': 'amountTest',
        'description': 'testing description',
        'kelas' : 'PBP2'
    }

    return render(request, "main.html", context)