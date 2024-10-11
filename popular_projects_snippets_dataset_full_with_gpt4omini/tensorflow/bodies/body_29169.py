# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
value_structure = tensor_spec.TensorSpec([], dtypes.float32)
opt = optional_ops.Optional.empty(value_structure)
self.assertTrue(opt.element_spec.is_compatible_with(value_structure))
self.assertFalse(
    opt.element_spec.is_compatible_with(
        tensor_spec.TensorSpec([1], dtypes.float32)))
self.assertFalse(
    opt.element_spec.is_compatible_with(
        tensor_spec.TensorSpec([], dtypes.int32)))
self.assertFalse(self.evaluate(opt.has_value()))
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(opt.get_value())
