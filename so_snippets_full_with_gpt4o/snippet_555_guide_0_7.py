import django # pragma: no cover
from django.test.client import RequestFactory # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
from l3.Runtime import _l_
try:
    from django.http import JsonResponse
    _l_(14112)

except ImportError:
    pass

def your_view(request):
    _l_(14115)

    json_object = {'key': "value"}
    _l_(14113)
    aux = JsonResponse(json_object)
    _l_(14114)
    return aux

