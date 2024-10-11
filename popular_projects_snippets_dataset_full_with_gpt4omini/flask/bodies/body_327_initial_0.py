from flask import Flask # pragma: no cover

options = {'endpoint': 'my_endpoint'} # pragma: no cover
self = type('Mock', (object,), {'add_url_rule': lambda self, rule, endpoint, f, **options: None})() # pragma: no cover
rule = '/my_rule' # pragma: no cover
f = lambda: 'Hello, World!' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
endpoint = options.pop("endpoint", None)
_l_(4573)
self.add_url_rule(rule, endpoint, f, **options)
_l_(4574)
aux = f
_l_(4575)
exit(aux)
