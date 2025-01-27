# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
seq_input = ops.convert_to_tensor(seq_input_arg)
context_input = ops.convert_to_tensor(np.arange(100).reshape(10, 10))
seq_input = math_ops.cast(seq_input, dtype=dtypes.float32)
context_input = math_ops.cast(context_input, dtype=dtypes.float32)
with self.assertRaisesRegex(ValueError, 'sequence_input must have rank 3'):
    sfc.concatenate_context_input(context_input, seq_input)
