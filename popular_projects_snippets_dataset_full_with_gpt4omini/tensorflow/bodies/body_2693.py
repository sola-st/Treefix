# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
input_array = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=dtype)
c = self._NewComputation()
ops.Reduce(
    c,
    operands=[ops.Constant(c, input_array)],
    init_values=[ops.Constant(c, dtype(0))],
    computation=self._CreateBinaryAddComputation(dtype),
    dimensions_to_reduce=[dim])
self._ExecuteAndCompareClose(c, expected=[np.sum(input_array, axis=dim)])
