class MockSession: # pragma: no cover
    def __enter__(self): # pragma: no cover
        self.sess = tf.compat.v1.Session() # pragma: no cover
        return self.sess # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        self.sess.close() # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def session(self): # pragma: no cover
        return MockSession() # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not issubclass(exc_type, exception): # pragma: no cover
                    return False # pragma: no cover
                self.exception = exc_value # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    def assertIn(self, member, container): # pragma: no cover
        assert member in container # pragma: no cover
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
