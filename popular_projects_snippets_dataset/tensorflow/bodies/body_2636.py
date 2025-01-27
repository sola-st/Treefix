# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Ne(
    ops.Constant(c, NumpyArrayS32([1, 2, 3, 4])),
    ops.Constant(c, NumpyArrayS32([4, 2, 3, 1])))
self._ExecuteAndCompareExact(c, expected=[[True, False, False, True]])

ops.Ne(
    ops.Constant(c, NumpyArrayF32([-2.0, 0.0,
                                   float("nan"),
                                   float("nan")])),
    ops.Constant(c, NumpyArrayF32([2.0, -0.0, 1.0,
                                   float("nan")])))
self._ExecuteAndAssertWith(
    np.testing.assert_allclose,
    c, (),
    expected=[[True, False, True, True]])
