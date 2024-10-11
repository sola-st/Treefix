# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
encoded = composite_tensor_ops.composite_tensor_to_variants(value())
with self.assertRaisesRegex(errors.InvalidArgumentError, message):
    self.evaluate(
        composite_tensor_ops.composite_tensor_from_variant(encoded, spec))
