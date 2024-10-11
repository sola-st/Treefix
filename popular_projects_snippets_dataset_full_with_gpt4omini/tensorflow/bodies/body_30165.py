# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
self.tensor_type = tensor_type
self.test = test
self._use_resource = use_resource

self.x_np = np.array(x).astype(tensor_type.as_numpy_dtype)
# Give the value a non-zero imaginary component for complex types.
if tensor_type.is_complex:
    self.x_np -= 1j * self.x_np
self.x = constant_op.constant(self.x_np, dtype=tensor_type)
