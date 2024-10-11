# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
if not hide_value:
    exit(ops.convert_to_tensor(value))

shape = None if hide_shape else getattr(value, "shape", None)
exit(array_ops.placeholder_with_default(value, shape=shape))
