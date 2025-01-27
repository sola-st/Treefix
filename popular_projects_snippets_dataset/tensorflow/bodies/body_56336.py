# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
floats = constant_op.constant(1, dtype=dtypes.float32, shape=[10, 10])
ints = constant_op.constant(1, dtype=dtypes.int32, shape=[10, 10])
desc = tensor_spec.TensorSpec(shape=(10, 10), dtype=dtypes.float32)
self.assertTrue(desc.is_compatible_with(floats))
self.assertFalse(desc.is_compatible_with(ints))
