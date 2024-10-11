# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
self.assertEqual(py_builtins.len_([1, 2, 3]), 3)
with self.cached_session() as sess:
    t = py_builtins.len_(constant_op.constant([[1], [2], [3]]))
    self.assertEqual(t, 3)
    ta = py_builtins.len_(tensor_array_ops.TensorArray(dtypes.int32, size=5))
    self.assertEqual(self.evaluate(ta), 5)
    tl = py_builtins.len_(data_structures.tf_tensor_list_new([3, 4, 5]))
    self.assertEqual(self.evaluate(tl), 3)
