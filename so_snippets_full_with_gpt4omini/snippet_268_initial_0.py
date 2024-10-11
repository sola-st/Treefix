 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering
from l3.Runtime import _l_
results = Model.objects.filter(x=5).exclude(a=True)
_l_(971)

