# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.GetTupleElement(
    ops.Tuple(c, [
        ops.Constant(c, np.int32(42)),
        ops.Constant(c, NumpyArrayF32([1.0, 2.0])),
        ops.Constant(c, NumpyArrayBool([True, False, False, True]))
    ]), 1)
self._ExecuteAndCompareClose(c, expected=[[1.0, 2.0]])
