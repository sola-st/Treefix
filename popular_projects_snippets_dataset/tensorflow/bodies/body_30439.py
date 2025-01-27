# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
exit(array_ops.pad(
    x,
    ops.convert_to_tensor(a, paddings_dtype),
    mode=mode,
    constant_values=constant_values))
