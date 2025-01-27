# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
ragged_cross = ragged_array_ops.cross(inputs)
ragged_cross_hashed = ragged_array_ops.cross_hashed(inputs, num_buckets,
                                                    hash_key)

if expected is not None:
    self.assertAllEqual(ragged_cross, expected)
if expected_hashed is not None:
    self.assertAllEqual(ragged_cross_hashed, expected_hashed)

if matches_sparse_cross:
    # Check that ragged.cross & sparse.cross match.
    sparse_inputs = [self._ragged_to_sparse(t) for t in inputs]
    sparse_cross = sparse_ops.sparse_cross(sparse_inputs)
    self.assertAllEqual(ragged_cross,
                        ragged_tensor.RaggedTensor.from_sparse(sparse_cross))

    # Check that ragged.cross_hashed & sparse.cross_hashed match.
    sparse_inputs = [self._ragged_to_sparse(t) for t in inputs]
    sparse_cross_hashed = sparse_ops.sparse_cross_hashed(
        sparse_inputs, num_buckets, hash_key)
    self.assertAllEqual(
        ragged_cross_hashed,
        ragged_tensor.RaggedTensor.from_sparse(sparse_cross_hashed))
