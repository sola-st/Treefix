import unittest # pragma: no cover

class MockSession: # pragma: no cover
    def __enter__(self): # pragma: no cover
        return tf.Session() # pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
class TestCaseMock(unittest.TestCase): # pragma: no cover
    def session(self): # pragma: no cover
        return MockSession() # pragma: no cover
 # pragma: no cover
test_case = TestCaseMock() # pragma: no cover

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
