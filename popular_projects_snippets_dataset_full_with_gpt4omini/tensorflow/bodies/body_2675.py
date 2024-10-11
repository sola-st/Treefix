# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
a = np.arange(9).astype(np.int32).reshape((3, 3))
indices = np.array([[[0, 2], [2, 1]], [[1, 2], [2, 0]]], dtype=np.int32)
dnums = xla_client.GatherDimensionNumbers()
dnums.offset_dims.append(1)
dnums.offset_dims.append(2)
dnums.start_index_map.append(0)
dnums.start_index_map.append(1)
dnums.index_vector_dim = 2
c = self._NewComputation()
ops.Gather(
    ops.Constant(c, a),
    ops.Constant(c, indices),
    dnums,
    slice_sizes=[1, 1])
g, = self._Execute(c, ())
expected = np.array([[[[2, 7]]], [[[5, 6]]]], dtype=np.int32)
np.testing.assert_allclose(g, expected, rtol=1e-4)
