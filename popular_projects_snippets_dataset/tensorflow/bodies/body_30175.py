# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
y = x + 1
exit(gen_array_ops.tensor_strided_slice_update(y, [0], [1], [1], [0]))
