# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/py_func_test.py

side_counter = [0]

def test_fn(_):
    side_counter[0] += 1

with self.cached_session() as sess:
    result = py_func.wrap_py_func(test_fn, None, (5,), use_dummy_return=True)
    self.assertEqual(1, self.evaluate(result))
    self.assertEqual([1], side_counter)
    result = py_func.wrap_py_func(
        test_fn, None, (constant_op.constant(5),), use_dummy_return=True)
    self.assertEqual(1, self.evaluate(result))
    self.assertEqual([2], side_counter)
