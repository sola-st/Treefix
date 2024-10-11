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
