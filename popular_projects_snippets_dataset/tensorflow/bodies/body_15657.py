# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    'sparse indices and values must have the same length'):
    self.evaluate(gen_ragged_array_ops.RaggedCross(
        ragged_values=[],
        ragged_row_splits=[],
        sparse_indices=[[5]],
        sparse_values=[],
        sparse_shape=[5],
        dense_inputs=[['a']],
        input_order='RD',
        hashed_output=False,
        num_buckets=5,
        hash_key=2,
        out_values_type=dtypes.string,
        out_row_splits_type=dtypes.int64))
