# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
x = np.array([0.53787335, 0.24015466, 0.47494545, 0.13567594, 0.95114538],
             dtype=dtype)
a = np.array([0.00753073, 0.34813385, 0.30485708, 1.29298632, 0.51472606],
             dtype=dtype)
b = np.array([0.55688389, 0.59794214, 0.42661022, 1.59748339, 0.95047677],
             dtype=dtype)
c = self._NewComputation()
ops.RegularizedIncompleteBeta(
    ops.Constant(c, a), ops.Constant(c, b), ops.Constant(c, x))
expected = np.array(
    [0.98923271, 0.48575411, 0.57952568, 0.12579775, 0.96989155])
self._ExecuteAndCompareClose(c, expected=[expected], rtol=2e-2)
