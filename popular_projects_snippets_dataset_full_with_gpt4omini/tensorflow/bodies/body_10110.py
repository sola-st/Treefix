# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
slc = indexed_slices.IndexedSlices(
    array_ops.constant([1, 2], shape=[1, 2]), array_ops.constant([1]),
    array_ops.constant([2, 2]))
slc_as_dense = np.array([[0, 0], [1, 2]])
with test_util.use_gpu():
    # add_n currently always converts IndexedSlices to dense
    self.assertAllEqual(slc_as_dense, math_ops.add_n([slc]))
    self.assertAllEqual(2 * slc_as_dense, math_ops.add_n([slc, slc]))
