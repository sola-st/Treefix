import sys # pragma: no cover
import types # pragma: no cover

class MockPatch: # pragma: no cover
    def __init__(self, target): # pragma: no cover
        self.target = target # pragma: no cover
    def __call__(self, func): # pragma: no cover
        return func # pragma: no cover
class MockModule(types.ModuleType): # pragma: no cover
    def patch(self, target): # pragma: no cover
        return MockPatch(target) # pragma: no cover
guineapig = MockModule('guineapig') # pragma: no cover
gorilla = MockModule('gorilla') # pragma: no cover
sys.modules['gorilla'] = gorilla # pragma: no cover
sys.modules['guineapig'] = guineapig # pragma: no cover

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

