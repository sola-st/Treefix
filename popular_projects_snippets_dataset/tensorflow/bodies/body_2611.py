# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
rng = np.random.RandomState(0)
lhs = NumpyArrayF32(rng.randn(10, 3, 4))
rhs = NumpyArrayF32(rng.randn(10, 4, 5))

dimension_numbers = xla_client.DotDimensionNumbers()
dimension_numbers.lhs_contracting_dimensions.append(2)
dimension_numbers.rhs_contracting_dimensions.append(1)
dimension_numbers.lhs_batch_dimensions.append(0)
dimension_numbers.rhs_batch_dimensions.append(0)

ops.DotGeneral(
    ops.Constant(c, lhs), ops.Constant(c, rhs), dimension_numbers)
self._ExecuteAndCompareClose(c, expected=[np.matmul(lhs, rhs)], rtol=1e-6)
