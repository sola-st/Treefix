# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/stats.py
from l3.Runtime import _l_
size = 0
_l_(18315)
for key, value in headers.items():
    _l_(18319)

    if isinstance(value, (list, tuple)):
        _l_(18318)

        for v in value:
            _l_(18317)

            size += len(b": ") + len(key) + len(v)
            _l_(18316)
aux = size + len(b'\r\n') * (len(headers.keys()) - 1)
_l_(18320)
exit(aux)
