# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Map(c,
        [ops.Constant(c, np.array([1.0, 2.0, 3.0, 4.0], dtype=in_dtype))],
        self._CreateConstantComputation(in_dtype, out_dtype), [0])
self._ExecuteAndCompareExact(c, expected=[[1, 1, 1, 1]])
