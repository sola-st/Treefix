from unittest.mock import patch, MagicMock # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict-or-any-other-python-object
from l3.Runtime import _l_
try:
    import pickle
    _l_(13723)

except ImportError:
    pass

a = {'hello': 'world'}
_l_(13724)

with open('filename.pickle', 'wb') as handle:
    _l_(13726)

    pickle.dump(a, handle)
    _l_(13725)

with open('filename.pickle', 'rb') as handle:
    _l_(13728)

    b = pickle.load(handle)
    _l_(13727)
try:
    from anycache import anycache
    _l_(13730)

except ImportError:
    pass

@anycache(cachedir='path/to/files')
def myfunc(hello):
    _l_(13732)

    aux = {'hello', hello}
    _l_(13731)
    return aux

