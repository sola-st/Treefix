import numpy as np # pragma: no cover

self = type('Mock', (object,), {'_testSimpleHelper': lambda self, dtype, val: None})() # pragma: no cover
dtypes = type('Mock', (object,), {'string': np.str_})() # pragma: no cover

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
_l_(21902)
