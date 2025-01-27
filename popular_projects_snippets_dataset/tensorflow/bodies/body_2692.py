# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.Reduce(
    c,
    operands=[
        ops.Constant(c, np.array([1.0, 2.0, 3.0, 4.0], dtype=dtype))
    ],
    init_values=[ops.Constant(c, dtype(0))],
    computation=self._CreateBinaryAddComputation(dtype),
    dimensions_to_reduce=[0])
self._ExecuteAndCompareClose(c, expected=[10])
