client_id = 1 # pragma: no cover

from datetime import datetime # pragma: no cover

client_id = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
from l3.Runtime import _l_
Reserved.objects.all().filter(client=client_id).order_by('check_in')
_l_(3477)

Reserved.objects.all().filter(client=client_id).order_by('-check_in')
_l_(3478)

