import random # pragma: no cover
from urllib.parse import urlencode # pragma: no cover

_getarg = lambda request, key, default, cast: cast(request.args.get(key.decode(), default)) # pragma: no cover
class MockRequest: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.args = {'total': '150', 'show': '5'} # pragma: no cover
    def write(self, data): # pragma: no cover
        print(data.decode()) # pragma: no cover
request = MockRequest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/benchserver.py
from l3.Runtime import _l_
total = _getarg(request, b'total', 100, int)
_l_(6046)
show = _getarg(request, b'show', 10, int)
_l_(6047)
nlist = [random.randint(1, total) for _ in range(show)]
_l_(6048)
request.write(b"<html><head></head><body>")
_l_(6049)
args = request.args.copy()
_l_(6050)
for nl in nlist:
    _l_(6054)

    args['n'] = nl
    _l_(6051)
    argstr = urlencode(args, doseq=True)
    _l_(6052)
    request.write(f"<a href='/follow?{argstr}'>follow {nl}</a><br>"
                  .encode('utf8'))
    _l_(6053)
request.write(b"</body></html>")
_l_(6055)
aux = b''
_l_(6056)
exit(aux)
