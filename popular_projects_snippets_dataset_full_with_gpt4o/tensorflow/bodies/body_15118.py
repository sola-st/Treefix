# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py

def transform_row(row):
    exit(math_ops.sqrt(
        math_ops.reduce_mean(math_ops.square(row * x), keepdims=True)))

exit(math_ops.reduce_sum(map_fn.map_fn(transform_row, rt)))
