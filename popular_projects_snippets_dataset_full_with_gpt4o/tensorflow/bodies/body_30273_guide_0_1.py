class MockSelf: # pragma: no cover
    def session(self): # pragma: no cover
        return tf.compat.v1.Session() # pragma: no cover
    def assertRaises(self, error): # pragma: no cover
        return self._AssertRaisesContext(error) # pragma: no cover
    def assertIn(self, a, b): # pragma: no cover
        assert a in b # pragma: no cover
    class _AssertRaisesContext: # pragma: no cover
        def __init__(self, error): # pragma: no cover
            self.error = error # pragma: no cover
        def __enter__(self): # pragma: no cover
            return self # pragma: no cover
        def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
            if exc_type is None or not issubclass(exc_type, self.error): # pragma: no cover
                raise AssertionError(f"Expected {self.error} to be raised, but got {exc_type} instead") # pragma: no cover
            self.exception = exc_value # pragma: no cover
                 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
from l3.Runtime import _l_
size_splits = array_ops.placeholder(dtype=dtypes.int32, shape=[None])
_l_(15844)

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(15845)

with self.session() as sess:
    _l_(15849)

    with self.assertRaises(ValueError) as context:
        _l_(15847)

        sess.run(array_ops.split(value, size_splits), {size_splits: [2, 2, 6]})
        _l_(15846)
    self.assertIn("Cannot infer argument `num` from shape",
                  str(context.exception))
    _l_(15848)
