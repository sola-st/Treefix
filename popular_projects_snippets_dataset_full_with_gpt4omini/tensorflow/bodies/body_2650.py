# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
c = self._NewComputation()
ops.ReducePrecision(
    ops.Constant(c, NumpyArrayF32([float.fromhex("0x1.32fffep-3")])),
    exponent_bits=8,
    mantissa_bits=7)
self._ExecuteAndCompareClose(c, expected=[[float.fromhex("0x1.32p-3")]])
