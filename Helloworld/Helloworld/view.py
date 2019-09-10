from django.shortcuts import render


def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)

