# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
# For the first shape:
# First batch:
# [?   e.]
# [1.  ? ]
# Second batch:
# [e   ? ]
# [e   e ]
#
# The softmax results should be:
# [?   1.]     [1    ?]
# [1.  ? ] and [.5  .5]
# where ? means implicitly zero.
#
# The second shape: same input data, but with a higher-rank shape.
shapes = [[2, 2, 2], [2, 1, 2, 2]]
for shape in shapes:
    values = np.asarray(
        [0., np.e, 1., 0., np.e, 0., np.e, np.e]).reshape(shape)
    sp_t, unused_nnz = _sparsify(values, thresh=1e-2)
    expected_values = [1., 1., 1., .5, .5]

    with test_util.force_cpu():
        result = sparse_ops.sparse_softmax(sp_t)

        self.assertAllEqual(expected_values, result.values)
        self.assertAllEqual(sp_t.indices, result.indices)
        self.assertAllEqual(shape, result.dense_shape)
