import warnings # pragma: no cover
import pandas as pd # pragma: no cover

def h(x, *, keyword_arg=None): return x # pragma: no cover
warnings = type('MockWarnings', (object,), {'catch_warnings': warnings.catch_warnings, 'simplefilter': warnings.simplefilter})() # pragma: no cover

import warnings # pragma: no cover
import pandas as pd # pragma: no cover

def h(x, *, keyword_arg=None): return x # pragma: no cover
class MockWarnings:  # Mock class to simulate warnings module # pragma: no cover
    def catch_warnings(self, record=False): # pragma: no cover
        class MockContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return [] # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                pass # pragma: no cover
        return MockContextManager() # pragma: no cover
    def simplefilter(self, action): # pragma: no cover
        valid_actions = ('error', 'ignore', 'always', 'default', 'module') # pragma: no cover
        if action not in valid_actions: # pragma: no cover
            raise AssertionError(f"invalid action: {action}") # pragma: no cover
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
