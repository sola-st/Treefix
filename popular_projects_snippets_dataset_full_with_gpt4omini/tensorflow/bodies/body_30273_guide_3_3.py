class MockSession: # Mocking the session context manager # pragma: no cover
    def __enter__(self): return self # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): pass # pragma: no cover
    def run(self, fetches, feed_dict=None): raise ValueError('Cannot infer argument `num` from shape') # pragma: no cover
 # pragma: no cover
class MockTestCase: # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): return self # pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
                if exc_type is not exception: return False # pragma: no cover
                self.exception = exc_val # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    def assertIn(self, member, container): # pragma: no cover
        if member not in container: # pragma: no cover
            raise AssertionError(f'{member} not in {container}') # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
from l3.Runtime import _l_
size_splits = array_ops.placeholder(dtype=dtypes.int32, shape=[None])
_l_(4390)

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(4391)

with self.session() as sess:
    _l_(4395)

    with self.assertRaises(ValueError) as context:
        _l_(4393)

        sess.run(array_ops.split(value, size_splits), {size_splits: [2, 2, 6]})
        _l_(4392)
    self.assertIn("Cannot infer argument `num` from shape",
                  str(context.exception))
    _l_(4394)
