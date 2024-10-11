# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
a = np.arange(9).astype(np.int32).reshape((3, 3))
scatter_indices = np.array([0, 2], dtype=np.int32)
updates = np.array([[10, 20, 30], [70, 80, 90]], dtype=np.int32)

dnums = xla_client.ScatterDimensionNumbers()
dnums.update_window_dims.append(1)
dnums.inserted_window_dims.append(0)
dnums.scatter_dims_to_operand_dims.append(0)
dnums.index_vector_dim = 1

c = self._NewComputation()
ops.Scatter(
    ops.Constant(c, a), ops.Constant(c, scatter_indices),
    ops.Constant(c, updates), self._CreateBinaryAddComputation(np.int32),
    dnums)
expected = np.array([[10, 21, 32], [3, 4, 5], [76, 87, 98]],
                    dtype=np.int32)
self._ExecuteAndCompareClose(c, expected=[expected])
