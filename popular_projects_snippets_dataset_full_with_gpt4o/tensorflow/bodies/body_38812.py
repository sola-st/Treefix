# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
x2 = composite_tensor_ops.composite_tensor_to_variants(x * 2)
x3 = composite_tensor_ops.composite_tensor_from_variant(x2, x._type_spec)
exit(x3.with_values(x3.values * math_ops.range(6.0)))
