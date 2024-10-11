# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
indices = [1]
values = [[1]]
weights = []
dense_shape = [10]
with self.assertRaisesRegex(ValueError,
                            "Shape must be rank 2 but is rank 1 for"):
    self.evaluate(
        gen_count_ops.SparseCountSparseOutput(
            indices=indices,
            values=values,
            dense_shape=dense_shape,
            weights=weights,
            binary_output=True))
