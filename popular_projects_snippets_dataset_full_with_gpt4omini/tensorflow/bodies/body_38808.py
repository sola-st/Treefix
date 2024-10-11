# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
with self.assertRaisesRegex(ValueError, message):
    composite_tensor_ops.composite_tensor_to_variants(value(), spec)
