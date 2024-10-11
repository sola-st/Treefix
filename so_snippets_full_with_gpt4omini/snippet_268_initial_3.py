class MockQuerySet:  # Mock for QuerySet# pragma: no cover
    def filter(self, **kwargs): return self# pragma: no cover
    def exclude(self, **kwargs): return self# pragma: no cover
# pragma: no cover
class MockModel:  # Mock for Model# pragma: no cover
    objects = MockQuerySet()# pragma: no cover
# pragma: no cover
Model = MockModel # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering
from l3.Runtime import _l_
results = Model.objects.filter(x=5).exclude(a=True)
_l_(971)

