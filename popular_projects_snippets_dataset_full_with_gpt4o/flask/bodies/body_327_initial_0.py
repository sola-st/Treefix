from typing import Dict, Callable # pragma: no cover

options: Dict[str, str] = {'key1': 'value1', 'key2': 'value2', 'endpoint': 'test_endpoint'} # pragma: no cover
rule: str = '/example' # pragma: no cover
f: Callable = lambda: 'function response' # pragma: no cover
self = type('Mock', (object,), {'add_url_rule': lambda self, rule, endpoint, f, **options: print('URL rule added')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
endpoint = options.pop("endpoint", None)
_l_(22519)
self.add_url_rule(rule, endpoint, f, **options)
_l_(22520)
aux = f
_l_(22521)
exit(aux)
