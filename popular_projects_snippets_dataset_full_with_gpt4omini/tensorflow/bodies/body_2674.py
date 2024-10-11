# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
a = ops.Constant(c, np.int32(3))
b = ops.Constant(c, np.int32(1))
x = ops.Parameter(c, 0, xla_client.shape_from_pyval(NumpyArrayS32(0)))
const_expr = ops.Sub(b, a)
non_const_expr = ops.Mul(const_expr, x)
self.assertTrue(c.is_constant(const_expr))
self.assertFalse(c.is_constant(non_const_expr))
