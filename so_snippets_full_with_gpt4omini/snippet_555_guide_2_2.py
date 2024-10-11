class MockRequest(object): pass # pragma: no cover
request = MockRequest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
from l3.Runtime import _l_
try:
    from django.http import JsonResponse
    _l_(1929)

except ImportError:
    pass

def your_view(request):
    _l_(1932)

    json_object = {'key': "value"}
    _l_(1930)
    aux = JsonResponse(json_object)
    _l_(1931)
    return aux

