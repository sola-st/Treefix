# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/map_fn_test.py
with context.eager_mode():
    dtype = map_fn.map_fn(lambda x: constant_op.constant(""),
                          constant_op.constant([]),
                          dtype=dtypes.string).dtype
    self.assertEqual(dtype, dtypes.string)
