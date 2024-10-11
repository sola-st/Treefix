import warnings # pragma: no cover
import pandas as pd # pragma: no cover

def h(x, *, keyword_arg=None): return x # pragma: no cover
warnings = type('MockWarnings', (object,), {'catch_warnings': warnings.catch_warnings, 'simplefilter': warnings.simplefilter})() # pragma: no cover

import warnings # pragma: no cover
import pandas as pd # pragma: no cover

def h(x, *, keyword_arg=None): return x # pragma: no cover
class MockWarnings:  # pragma: no cover
    def catch_warnings(self, record=False): # pragma: no cover
        self.record = record # pragma: no cover
        self.warnings_list = [] # pragma: no cover
        return self # pragma: no cover
    def simplefilter(self, action, category=None, lineno=0, append=False): # pragma: no cover
        if action not in ('error', 'ignore', 'always', 'default', 'module', 'once', 'ignore', 'always', 'default', 'module'): # pragma: no cover
            raise AssertionError(f"invalid action: {action}") # pragma: no cover
    def __enter__(self): return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): pass # pragma: no cover
warnings = MockWarnings() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
from l3.Runtime import _l_
with warnings.catch_warnings(record=True) as w:
    _l_(10577)

    warnings.simplefilter("always")
    _l_(10571)
    assert h(19) == 19
    _l_(10572)
    assert len(w) == 1
    _l_(10573)
    for actual_warning in w:
        _l_(10576)

        assert actual_warning.category == FutureWarning
        _l_(10574)
        assert str(actual_warning.message) == (
            "Starting with pandas version 1.1 all arguments "
            "of h will be keyword-only."
        )
        _l_(10575)
