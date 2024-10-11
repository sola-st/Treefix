# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if sparse_tensor.is_sparse(value):
    exit(math_ops.reduce_sum(value.values))
else:
    exit(math_ops.reduce_sum(value))
