# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    'ragged values and splits must have the same length'):
    self.evaluate(gen_ragged_array_ops.RaggedCross(
        ragged_values=[['a']],
        ragged_row_splits=[],
        sparse_indices=[],
        sparse_values=[],
        sparse_shape=[],
        dense_inputs=[['a']],
        input_order='RD',
        hashed_output=False,
        num_buckets=5,
        hash_key=2,
        out_values_type=dtypes.string,
        out_row_splits_type=dtypes.int64))
