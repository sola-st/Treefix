# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
seq_input = ops.convert_to_tensor(np.arange(12).reshape(2, 3, 2))
context_input = ops.convert_to_tensor(np.arange(10).reshape(2, 5))
seq_input = math_ops.cast(seq_input, dtype=dtypes.float32)
context_input = math_ops.cast(context_input, dtype=dtypes.float32)
input_layer = sfc.concatenate_context_input(context_input, seq_input)

expected = np.array([
    [[0, 1, 0, 1, 2, 3, 4], [2, 3, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3, 4]],
    [[6, 7, 5, 6, 7, 8, 9], [8, 9, 5, 6, 7, 8, 9], [10, 11, 5, 6, 7, 8, 9]]
], dtype=np.float32)
output = self.evaluate(input_layer)
self.assertAllEqual(expected, output)
