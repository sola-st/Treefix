# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
splits = []
values = [1, 1, 2, 1, 2, 10, 5]
weights = [1, 2, 3, 4, 5, 6, 7]
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Must provide at least 2 elements for the splits argument"):
    self.evaluate(
        gen_count_ops.RaggedCountSparseOutput(
            splits=splits,
            values=values,
            weights=weights,
            binary_output=False))
