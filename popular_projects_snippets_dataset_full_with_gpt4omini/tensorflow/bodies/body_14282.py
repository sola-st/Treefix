# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
indices = [[0, 0], [0, 1], [1, 0]]
values = [1, 1, 1, 10]
weights = [1, 2, 4, 6]
dense_shape = [2, 3]
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Number of values must match first dimension of indices"):
    self.evaluate(
        gen_count_ops.SparseCountSparseOutput(
            indices=indices,
            values=values,
            dense_shape=dense_shape,
            weights=weights,
            binary_output=False))
