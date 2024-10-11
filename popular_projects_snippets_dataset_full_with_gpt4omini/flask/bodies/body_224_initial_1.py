from typing import List # pragma: no cover

value = ['item1', 'item2', 'item3'] # pragma: no cover
self = type('Mock', (), {'serializer': type('Mock', (), {'tag': lambda self, item: f'tagged_{item}'})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
aux = [self.serializer.tag(item) for item in value]
_l_(8254)
exit(aux)
