# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
splits = [0, 4, 7]
values = [1, 1, 2, 1, 2, 10, 5]
weights = [1, 2, 3, 4, 5, 6]
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Weights and values must have the same shape"):
    self.evaluate(
        gen_count_ops.RaggedCountSparseOutput(
            splits=splits,
            values=values,
            weights=weights,
            binary_output=False))
