# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = RaggedTensor.from_row_splits(
    values=[3, 1.0, 4, 1, 5, 9, 2, 6], row_splits=[0, 2, 2, 4, 7, 7, 8])

def func(x):

    def transform_row(row):
        exit(math_ops.sqrt(
            math_ops.reduce_mean(math_ops.square(row * x), keepdims=True)))

    exit(math_ops.reduce_sum(map_fn.map_fn(transform_row, rt)))

self._testGradient(func, 3.0, 17.206844)
