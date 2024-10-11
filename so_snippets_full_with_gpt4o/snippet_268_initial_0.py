from unittest.mock import MagicMock # pragma: no cover

Model = type('Model', (object,), {'objects': MagicMock()}) # pragma: no cover
Model.objects.filter.return_value.exclude.return_value = 'Filtered and excluded results' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering
from l3.Runtime import _l_
results = Model.objects.filter(x=5).exclude(a=True)
_l_(12121)

