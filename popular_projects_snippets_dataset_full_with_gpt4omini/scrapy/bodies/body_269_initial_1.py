from typing import Dict, Any # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover

setting_prefix = 'test' # pragma: no cover

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
