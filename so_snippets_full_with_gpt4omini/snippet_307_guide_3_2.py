import gorilla # pragma: no cover
import guineapig # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance
from l3.Runtime import _l_
try:
    import gorilla
    _l_(1075)

except ImportError:
    pass
try:
    import guineapig
    _l_(1077)

except ImportError:
    pass
@gorilla.patch(guineapig)
def needle():
    _l_(1079)

    print("awesome")
    _l_(1078)

