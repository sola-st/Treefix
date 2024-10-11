from typing import List # pragma: no cover
import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._testSimpleHelper = lambda dt, tests: print(f'Testing with {dt}: {tests}') # pragma: no cover
class MockDtypes: pass # pragma: no cover
dtypes = MockDtypes() # pragma: no cover
dtypes.string = np.dtype('U') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unique_test.py
from l3.Runtime import _l_
self._testSimpleHelper(dtypes.string, [
    ([], []),
    (["hello"], ["hello"]),
    (["hello", "hello", "hello"], ["hello"]),
    (["hello", "world"], ["hello", "world"]),
    (["foo", "bar", "baz", "baz", "bar", "foo"], ["foo", "bar", "baz"]),
])
_l_(9538)
