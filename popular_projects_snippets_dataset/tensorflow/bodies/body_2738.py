# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
full_size = 5
c = self._NewComputation()
arg = np.array(reshape_size, dtype=np.int32)
expected = np.array(range(reshape_size), dtype=np.int32)
p = ops.Parameter(c, 0, xla_client.shape_from_pyval(arg))
ops.DynamicReshape(
    ops.Constant(c, NumpyArrayS32(range(full_size))), [p], [full_size],
    [True])
self._CompareToPyAndBufferProtocol(c, [arg], [expected],
                                   np.testing.assert_equal)
