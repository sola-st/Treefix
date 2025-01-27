# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
input_array = self._MakeSample3DArray(dtype)
c = self._NewComputation()
ops.Reduce(
    c,
    operands=[ops.Constant(c, input_array)],
    init_values=[ops.Constant(c, dtype(0))],
    computation=self._CreateBinaryAddComputation(dtype),
    dimensions_to_reduce=dims)
self._ExecuteAndCompareClose(c, expected=[np.sum(input_array, axis=dims)])
