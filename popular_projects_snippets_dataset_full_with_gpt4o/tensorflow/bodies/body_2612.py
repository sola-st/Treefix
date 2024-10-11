# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
rng = np.random.RandomState(0)
lhs = NumpyArrayF32(rng.randn(10, 3, 4))
rhs = NumpyArrayF32(rng.randn(10, 4, 5))
dimension_numbers = xla_client.make_dot_dimension_numbers(
    (([2], [1]), ([0], [0])))
config = xla_client.PrecisionConfig()
config.operand_precision.append(config.Precision.HIGH)
config.operand_precision.append(config.Precision.HIGHEST)
ops.DotGeneral(
    ops.Constant(c, lhs),
    ops.Constant(c, rhs),
    dimension_numbers,
    precision_config=config)
self._ExecuteAndCompareClose(c, expected=[np.matmul(lhs, rhs)], rtol=1e-6)
