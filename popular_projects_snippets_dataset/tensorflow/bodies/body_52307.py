# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
seq_input = ops.convert_to_tensor(np.arange(100).reshape(5, 5, 4))
context_input = ops.convert_to_tensor(np.arange(100).reshape(10, 10))
seq_input = math_ops.cast(seq_input, dtype=dtypes.float32)
with self.assertRaisesRegex(TypeError,
                            'context_input must have dtype float32'):
    sfc.concatenate_context_input(context_input, seq_input)
