# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
devices = ["/cpu:0", "/gpu:0"]
t0 = _make_indexed_slices([[1., 2.]], [1], [5, 2], devices[0])
t1 = _make_indexed_slices([[3., 4.], [5., 6.]], [1, 3], [5, 2], devices[1])
per_replica = value_lib.PerReplica((t0, t1))
result = cross_device_ops_lib._simple_reduce(
    per_replica, devices[0], math_ops.add_n, reduce_util.ReduceOp.SUM)

# Test that the result is semantically equal to both the concatenated
# IndexedSlices with and without duplicate indices.
total_with_dups = _make_indexed_slices(
    [[1., 2.], [3., 4.], [5., 6.]], [1, 1, 3], [5, 2], devices[0])
total_without_dups = _make_indexed_slices(
    [[4., 6.], [5., 6.]], [1, 3], [5, 2], devices[0])
self._assert_indexed_slices_equal(total_with_dups, result)
self._assert_indexed_slices_equal(total_without_dups, result)
