# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/lang/special_functions_test.py
l = special_functions.tensor_list(
    constant_op.constant([], dtype=dtypes.int32))
sl = list_ops.tensor_list_stack(l, element_dtype=dtypes.int32)
with self.cached_session() as sess:
    self.assertAllEqual(self.evaluate(sl), [])
