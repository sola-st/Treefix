# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
splits = [0, 4, 7]
values = [1, 1, 2, 1, -2, 10, 5]
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Input values must all be non-negative"):
    self.evaluate(
        gen_count_ops.RaggedCountSparseOutput(
            splits=splits, values=values, binary_output=False))
