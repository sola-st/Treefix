# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
tensor = constant_op.constant(42.0, dtype=dtypes.float32)
with self.assertRaises(ValueError):
    ops.convert_to_tensor(tensor, dtype=dtypes.int32)
