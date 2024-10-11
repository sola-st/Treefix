# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
with self.cached_session() as sess:
    dense_shape = [5, 2]
    t0 = _make_indexed_slices([[1., 2.]], [1], dense_shape, devices[0])
    t1 = _make_indexed_slices([[3., 4.], [5., 6.]], [1, 3], dense_shape,
                              devices[1])
    per_replica = value_lib.PerReplica((t0, t1))

    if batch_reduce:
        result = cross_device_ops_instance.batch_reduce(
            reduce_op, [(per_replica, per_replica)])
    else:
        result = cross_device_ops_instance.reduce(reduce_op, per_replica,
                                                  per_replica)

    total_indices_with_dups = [1, 1, 3]
    total_indices_without_dups = [1, 3]

    if reduce_op == reduce_util.ReduceOp.SUM:
        total_values_with_dups = [[1., 2.], [3., 4.], [5., 6.]]
        total_values_without_dups = [[4., 6.], [5., 6.]]
    else:
        assert reduce_op == reduce_util.ReduceOp.MEAN
        total_values_with_dups = [[0.5, 1.], [1.5, 2.], [2.5, 3.]]
        total_values_without_dups = [[2., 3.], [2.5, 3.]]

    total_mirrored_with_dups = _make_mirrored_indexed_slices(
        devices, total_values_with_dups, total_indices_with_dups, dense_shape)
    total_mirrored_without_dups = _make_mirrored_indexed_slices(
        devices, total_values_without_dups, total_indices_without_dups,
        dense_shape)

    # Test that the result is semantically equal to both the concatenated
    # IndexedSlices, as well as when the duplicate indices are summed up.
    if batch_reduce:
        total_mirrored_with_dups = [total_mirrored_with_dups]
        total_mirrored_without_dups = [total_mirrored_without_dups]

    self._assert_mirrored_equal(total_mirrored_with_dups, result, sess)
    self._assert_mirrored_equal(total_mirrored_without_dups, result, sess)
