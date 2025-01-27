# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
with self.session() as sess:
    # Compute a random rank-5 initial shape and new shape, randomly sparsify
    # it, and check that the output of SparseReshape has the same semantics
    # as a dense reshape.
    factors = np.array([2] * 4 + [3] * 4 + [5] * 4)  # 810k total elements
    orig_rank = np.random.randint(2, 7)
    orig_map = np.random.randint(orig_rank, size=factors.shape)
    orig_shape = [np.prod(factors[orig_map == d]) for d in range(orig_rank)]
    new_rank = np.random.randint(2, 7)
    new_map = np.random.randint(new_rank, size=factors.shape)
    new_shape = [np.prod(factors[new_map == d]) for d in range(new_rank)]

    orig_dense = np.random.uniform(size=orig_shape)
    orig_indices = np.transpose(np.nonzero(orig_dense < 0.5))
    orig_values = orig_dense[orig_dense < 0.5]

    new_dense = np.reshape(orig_dense, new_shape)
    new_indices = np.transpose(np.nonzero(new_dense < 0.5))
    new_values = new_dense[new_dense < 0.5]

    sp_input = self._SparseTensorPlaceholder()
    input_val = sparse_tensor.SparseTensorValue(orig_indices, orig_values,
                                                orig_shape)
    sp_output = sparse_ops.sparse_reshape(sp_input, new_shape)

    output_val = sess.run(sp_output, {sp_input: input_val})
    self.assertAllEqual(output_val.indices, new_indices)
    self.assertAllEqual(output_val.values, new_values)
    self.assertAllEqual(output_val.dense_shape, new_shape)
