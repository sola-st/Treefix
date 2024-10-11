import sys # pragma: no cover
class MockModule: pass # pragma: no cover

sys.modules['Desktop'] = MockModule() # pragma: no cover
sys.modules['Desktop'].test = MockModule() # pragma: no cover
sys.modules['Desktop'].test.__dict__.update({'__all__': [], 'function': lambda: 'mocked'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
from l3.Runtime import _l_
try:
    from Desktop.test import *
    _l_(2264)

except ImportError:
    pass

