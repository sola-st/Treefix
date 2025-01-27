# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
for t in [dtypes.uint64, dtypes.uint32, dtypes.int32, dtypes.int64]:
    self.assertEqual(constant_op.constant(t.max, dtype=t).numpy(), t.max)
    self.assertEqual(constant_op.constant(t.min, dtype=t).numpy(), t.min)
