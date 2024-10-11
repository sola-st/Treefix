from urllib.parse import urlencode # pragma: no cover
import random # pragma: no cover

_getarg = lambda req, key, default, typ: default # pragma: no cover
request = type('Mock', (object,), {'write': lambda self, data: print(data.decode()), 'args': {}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/benchserver.py
from l3.Runtime import _l_
total = _getarg(request, b'total', 100, int)
_l_(17474)
show = _getarg(request, b'show', 10, int)
_l_(17475)
nlist = [random.randint(1, total) for _ in range(show)]
_l_(17476)
request.write(b"<html><head></head><body>")
_l_(17477)
args = request.args.copy()
_l_(17478)
for nl in nlist:
    _l_(17482)

    args['n'] = nl
    _l_(17479)
    argstr = urlencode(args, doseq=True)
    _l_(17480)
    request.write(f"<a href='/follow?{argstr}'>follow {nl}</a><br>"
                  .encode('utf8'))
    _l_(17481)
request.write(b"</body></html>")
_l_(17483)
aux = b''
_l_(17484)
exit(aux)
