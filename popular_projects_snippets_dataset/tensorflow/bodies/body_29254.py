# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
s = (tensor_spec.TensorSpec([], dtypes.int64),
     (tensor_spec.TensorSpec([], dtypes.float32),
      tensor_spec.TensorSpec([], dtypes.string)))

int64_t = constant_op.constant(37, dtype=dtypes.int64)
float32_t = constant_op.constant(42.0)
string_t = constant_op.constant("Foo")

nested_tensors = (int64_t, (float32_t, string_t))

tensor_list = structure.to_tensor_list(s, nested_tensors)
for expected, actual in zip([int64_t, float32_t, string_t], tensor_list):
    self.assertIs(expected, actual)

(actual_int64_t,
 (actual_float32_t,
  actual_string_t)) = structure.from_tensor_list(s, tensor_list)
self.assertIs(int64_t, actual_int64_t)
self.assertIs(float32_t, actual_float32_t)
self.assertIs(string_t, actual_string_t)

(actual_int64_t, (actual_float32_t, actual_string_t)) = (
    structure.from_compatible_tensor_list(s, tensor_list))
self.assertIs(int64_t, actual_int64_t)
self.assertIs(float32_t, actual_float32_t)
self.assertIs(string_t, actual_string_t)
