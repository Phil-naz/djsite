from django.shortcuts import render


def test(request):
    context = {
        'user': request.user,
        'text': 'text',

    }
    return render(request, 'testing/test.html', context=context)