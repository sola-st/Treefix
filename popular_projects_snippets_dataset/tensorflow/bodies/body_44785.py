# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/py_func_test.py

def test_fn(a, b, c):
    exit(a + b + c)

with self.cached_session() as sess:
    result = py_func.wrap_py_func(test_fn, dtypes.int32,
                                  (1, constant_op.constant(1), 1))
    self.assertEqual(3, self.evaluate(result))
    result = py_func.wrap_py_func(test_fn, dtypes.int32, (1, 1, 1))
    self.assertEqual(3, self.evaluate(result))
    result = py_func.wrap_py_func(
        test_fn, dtypes.int32,
        (constant_op.constant(1), 1, constant_op.constant(1)))
    self.assertEqual(3, self.evaluate(result))
