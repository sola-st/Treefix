# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
arg0 = np.array([[1, 2, 3], [4, 5, 6]], dtype=dtype)
arg1 = np.array(2, dtype=np.int32)
expected = np.array([[1, 2], [4, 5]], dtype=np.int32)
c = self._NewComputation()
p0 = ops.Parameter(c, 0, xla_client.shape_from_pyval(arg0))
p1 = ops.Parameter(c, 1, xla_client.shape_from_pyval(arg1))
ops.DynamicReshape(p0, [p1, p1], [2, 3], [False, True])
self._CompareToPyAndBufferProtocol(c, [arg0, arg1], [expected],
                                   np.testing.assert_equal)
