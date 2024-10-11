from typing import Dict, Any, Optional # pragma: no cover

def without_none_values(d: Dict[str, Optional[Any]]) -> Dict[str, Any]: return {k: v for k, v in d.items() if v is not None} # pragma: no cover
class MockSettings:# pragma: no cover
    def getwithbase(self, prefix: str) -> Dict[str, Any]:# pragma: no cover
        return {'key1': 'value1', 'key2': None, 'key3': 'value3'} # pragma: no cover
self = type('Mock', (object,), {'settings': MockSettings()})() # pragma: no cover
setting_prefix = 'test_prefix' # pragma: no cover
def load_object(value: Any) -> Any: return value # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
from l3.Runtime import _l_
conf = without_none_values(self.settings.getwithbase(setting_prefix))
_l_(10015)
d = {}
_l_(10016)
for k, v in conf.items():
    _l_(10021)

    try:
        _l_(10020)

        d[k] = load_object(v)
        _l_(10017)
    except NotConfigured:
        _l_(10019)

        pass
        _l_(10018)
aux = d
_l_(10022)
exit(aux)
