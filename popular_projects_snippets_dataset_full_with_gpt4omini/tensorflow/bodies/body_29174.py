# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

with ops.device("/cpu:0"):
    optional_with_value = optional_ops.Optional.from_value(
        (constant_op.constant(37.0), constant_op.constant("Foo"),
         constant_op.constant(42)))
    optional_none = optional_ops.Optional.empty(
        tensor_spec.TensorSpec([], dtypes.float32))

with ops.device("/gpu:0"):
    gpu_optional_with_value = optional_ops._OptionalImpl(
        array_ops.identity(optional_with_value._variant_tensor),
        optional_with_value.element_spec)
    gpu_optional_none = optional_ops._OptionalImpl(
        array_ops.identity(optional_none._variant_tensor),
        optional_none.element_spec)

    gpu_optional_with_value_has_value = gpu_optional_with_value.has_value()
    gpu_optional_with_value_values = gpu_optional_with_value.get_value()

    gpu_optional_none_has_value = gpu_optional_none.has_value()

self.assertTrue(self.evaluate(gpu_optional_with_value_has_value))
self.assertEqual((37.0, b"Foo", 42),
                 self.evaluate(gpu_optional_with_value_values))
self.assertFalse(self.evaluate(gpu_optional_none_has_value))
