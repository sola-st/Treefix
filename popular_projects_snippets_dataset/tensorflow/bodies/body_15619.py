# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_sparse_op_test.py
# An empty vector, defined using a placeholder to ensure that we can't
# determine that it's invalid at graph-construction time.
empty_vector = array_ops.placeholder_with_default(
    array_ops.zeros([0], dtypes.int64), shape=None)

bad_rt1 = ragged_tensor.RaggedTensor.from_row_splits(
    row_splits=[2, 3], values=[1, 2, 3], validate=False)
bad_split0 = r'First value of ragged splits must be 0.*'
with self.assertRaisesRegex(errors.InvalidArgumentError, bad_split0):
    self.evaluate(bad_rt1.to_sparse())

bad_rt2 = ragged_tensor.RaggedTensor.from_row_splits(
    row_splits=[0, 5], values=empty_vector, validate=False)
bad_rt3 = ragged_tensor.RaggedTensor.from_row_splits(
    row_splits=[0, 1],
    values=ragged_tensor.RaggedTensor.from_row_splits(
        row_splits=[0, 5], values=empty_vector, validate=False),
    validate=False)
split_mismatch1_error = r'Final value of ragged splits must match.*'
for rt in [bad_rt2, bad_rt3]:
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                split_mismatch1_error):
        self.evaluate(rt.to_sparse())

bad_rt4 = ragged_tensor.RaggedTensor.from_row_splits(
    row_splits=[0, 5],
    values=ragged_tensor.RaggedTensor.from_row_splits(
        row_splits=[0], values=empty_vector, validate=False),
    validate=False)
split_mismatch2_error = r'Final value of ragged splits must match.*'
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            split_mismatch2_error):
    self.evaluate(bad_rt4.to_sparse())

bad_rt5 = ragged_tensor.RaggedTensor.from_row_splits(
    row_splits=empty_vector, values=[], validate=False)
empty_splits_error = (r'ragged splits may not be empty.*')
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            empty_splits_error):
    self.evaluate(bad_rt5.to_sparse())
