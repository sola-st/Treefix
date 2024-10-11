# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
values = [2, 3, 5, 7]
tensor = ops.convert_to_tensor(values, preferred_dtype=dtypes.float32)
self.assertEqual(dtypes.float32, tensor.dtype)

# Convert empty tensor to anything.
values = []
tensor = ops.convert_to_tensor(values, preferred_dtype=dtypes.int64)
self.assertEqual(dtypes.int64, tensor.dtype)

# The preferred dtype is a type error and will convert to
# float32 instead.
values = [1.23]
tensor = ops.convert_to_tensor(values, preferred_dtype=dtypes.int64)
self.assertEqual(dtypes.float32, tensor.dtype)
