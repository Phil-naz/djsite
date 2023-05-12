from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    context = {
    }
    return render(request, 'phil/about.html', context=context)


def about_analytics(request):
    context = {
    }
    return render(request, 'phil/about_analytics.html', context=context)


def about_django(request):
    context = {
    }
    return render(request, 'phil/about_django.html', context=context)

def fail(request):
    context = {
    }
    return render(request, 'phil/fail.html', context=context)
