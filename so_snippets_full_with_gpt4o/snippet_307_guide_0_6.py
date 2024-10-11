class Mock:# pragma: no cover
    pass # pragma: no cover
import types # pragma: no cover

guineapig = Mock() # pragma: no cover
def mock_patch(obj):# pragma: no cover
    def wrapper(func):# pragma: no cover
        setattr(obj, func.__name__, types.MethodType(func, obj))# pragma: no cover
        return func# pragma: no cover
    return wrapper # pragma: no cover
gorilla = Mock() # pragma: no cover
gorilla.patch = mock_patch # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance
from l3.Runtime import _l_
try:
    import gorilla
    _l_(13216)

except ImportError:
    pass
try:
    import guineapig
    _l_(13218)

except ImportError:
    pass
@gorilla.patch(guineapig)
def needle():
    _l_(13220)

    print("awesome")
    _l_(13219)

