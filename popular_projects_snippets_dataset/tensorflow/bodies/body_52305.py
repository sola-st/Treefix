# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
context_input = ops.convert_to_tensor(context_input_arg)
seq_input = ops.convert_to_tensor(np.arange(100).reshape(5, 5, 4))
seq_input = math_ops.cast(seq_input, dtype=dtypes.float32)
context_input = math_ops.cast(context_input, dtype=dtypes.float32)
with self.assertRaisesRegex(ValueError, 'context_input must have rank 2'):
    sfc.concatenate_context_input(context_input, seq_input)
