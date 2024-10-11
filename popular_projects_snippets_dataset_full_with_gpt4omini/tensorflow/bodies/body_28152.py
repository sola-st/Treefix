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
