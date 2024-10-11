from typing import Dict, Any # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
import json # pragma: no cover

def without_none_values(d: Dict[str, Any]) -> Dict[str, Any]:# pragma: no cover
    return {k: v for k, v in d.items() if v is not None} # pragma: no cover
setting_prefix = 'my_prefix' # pragma: no cover
def load_object(value: Any) -> Any:# pragma: no cover
    if value == 'invalid':# pragma: no cover
        raise NotConfigured('Invalid configuration')# pragma: no cover
    return value # pragma: no cover
self = type('Mock', (object,), {'settings': type('MockSettings', (object,), {'getwithbase': lambda self, prefix: {prefix + k: v for k, v in {"key1": "value1", "key2": None, "key3": "invalid", "key4": "value4"}.items()}})()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
from l3.Runtime import _l_
conf = without_none_values(self.settings.getwithbase(setting_prefix))
_l_(21131)
d = {}
_l_(21132)
for k, v in conf.items():
    _l_(21137)

    try:
        _l_(21136)

        d[k] = load_object(v)
        _l_(21133)
    except NotConfigured:
        _l_(21135)

        pass
        _l_(21134)
aux = d
_l_(21138)
exit(aux)
