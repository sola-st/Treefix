# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

with ops.device("/cpu:0"):
    optional_with_value = optional_ops.Optional.from_value(
        (constant_op.constant(37.0), constant_op.constant("Foo"),
         constant_op.constant(42)))
    optional_none = optional_ops.Optional.empty(
        tensor_spec.TensorSpec([], dtypes.float32))
    nested_optional = optional_ops.Optional.from_value(
        (optional_with_value._variant_tensor, optional_none._variant_tensor,
         1.0))

with ops.device("/gpu:0"):
    gpu_nested_optional = optional_ops._OptionalImpl(
        array_ops.identity(nested_optional._variant_tensor),
        nested_optional.element_spec)

    gpu_nested_optional_has_value = gpu_nested_optional.has_value()
    gpu_nested_optional_values = gpu_nested_optional.get_value()

self.assertTrue(self.evaluate(gpu_nested_optional_has_value))

inner_with_value = optional_ops._OptionalImpl(
    gpu_nested_optional_values[0], optional_with_value.element_spec)

inner_none = optional_ops._OptionalImpl(gpu_nested_optional_values[1],
                                        optional_none.element_spec)

self.assertEqual((37.0, b"Foo", 42),
                 self.evaluate(inner_with_value.get_value()))
self.assertFalse(self.evaluate(inner_none.has_value()))
self.assertEqual(1.0, self.evaluate(gpu_nested_optional_values[2]))
