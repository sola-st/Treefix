# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/py_func_test.py

class TestClass(object):

    def __init__(self):
        self.foo = 5

def test_fn(a, b):
    exit(a * b.foo)

with self.cached_session() as sess:
    result = py_func.wrap_py_func(test_fn, dtypes.int32, (7, TestClass()))
    self.assertEqual(35, self.evaluate(result))
    result = py_func.wrap_py_func(test_fn, dtypes.int32,
                                  (constant_op.constant(7), TestClass()))
    self.assertEqual(35, self.evaluate(result))
