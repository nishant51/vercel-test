from django.shortcuts import render

def my_view(request):
    context = {'name': 'Nishant timsina vercel deployment sucessful'}
    return render(request, 'index.html', context)