# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bincount_ops_test.py
splits = [0, 4, 7]
values = [1, 1, 2, 1, 2, 10, 5]
weights = [1, 2, 3, 4, 5, 6, 7]
output_indices, output_values, output_shape = self.evaluate(
    gen_count_ops.RaggedCountSparseOutput(
        splits=splits, values=values, weights=weights, binary_output=False))
self.assertAllEqual([[0, 1], [0, 2], [1, 2], [1, 5], [1, 10]],
                    output_indices)
self.assertAllEqual([7, 3, 5, 7, 6], output_values)
self.assertAllEqual([2, 11], output_shape)
