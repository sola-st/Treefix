# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
pred = ops.Constant(c, np.bool_(False))
true_operand = ops.Constant(c, np.float32(3.))
true_computation = self._CreateMulBy2Computation(np.float32)
false_operand = ops.Constant(c, np.float32(2.))
false_computation = self._CreateConstantComputation(
    np.float32, np.float32)
ops.Conditional(pred, true_operand, true_computation, false_operand,
                false_computation)
self._ExecuteAndCompareClose(c, expected=[1.])
