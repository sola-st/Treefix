import os # pragma: no cover
import pickle # pragma: no cover
class Mock: pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict-or-any-other-python-object
from l3.Runtime import _l_
try:
    import pickle
    _l_(1360)

except ImportError:
    pass

a = {'hello': 'world'}
_l_(1361)

with open('filename.pickle', 'wb') as handle:
    _l_(1363)

    pickle.dump(a, handle)
    _l_(1362)

with open('filename.pickle', 'rb') as handle:
    _l_(1365)

    b = pickle.load(handle)
    _l_(1364)
try:
    from anycache import anycache
    _l_(1367)

except ImportError:
    pass

@anycache(cachedir='path/to/files')
def myfunc(hello):
    _l_(1369)

    aux = {'hello', hello}
    _l_(1368)
    return aux

