# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
size = 0
_l_(7421)
for key, value in headers.items():
    _l_(7425)

    if isinstance(value, (list, tuple)):
        _l_(7424)

        for v in value:
            _l_(7423)

            size += len(b": ") + len(key) + len(v)
            _l_(7422)
aux = size + len(b'\r\n') * (len(headers.keys()) - 1)
_l_(7426)
exit(aux)
