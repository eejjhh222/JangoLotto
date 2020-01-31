from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {
        'round': 'round'
    }

    # return render(request, 'index.html', context)
    a = [1,2,3]
    b = [5,6,7]
    # b = b.__add__(a)
    # a.__iadd__([8,9])
    # a.append(b)
    # b = a.copy()
    # b = a.__delitem__(2)
    it = b.__iter__()
    print(a)
    print(next(it))

    return HttpResponse(a)

# if __name__ == '__main__':
#     index('')