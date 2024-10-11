# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = random_ops.random_uniform([2, 4])
t = numpy_util.pack_numpy(t, self.last_dimension_sharded_layout_2d)
with self.assertRaises(errors_impl.UnknownError):
    # Spliting over sharded dimension is not yet supported.
    _ = array_ops.split(t, [1, 1, 2], axis=1)
