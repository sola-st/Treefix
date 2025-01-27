# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
self.x_np = np.array(x).astype(tensor_type.as_numpy_dtype)
if tensor_type.is_bool:
    self.x_np = np.array(x % 3).astype(np.bool_)
# Give the value a non-zero imaginary component for complex types.
if tensor_type.is_complex:
    self.x_np -= 1j * self.x_np
self.test = test
self.x = constant_op.constant(self.x_np, dtype=tensor_type)
self.check_type_infer = check_type_infer
