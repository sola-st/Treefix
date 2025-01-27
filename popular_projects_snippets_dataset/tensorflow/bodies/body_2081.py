# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
arg = np.array([1 + 2**-2 + 2**-4, 128, 256], dtype=np.float32)
expected = np.array([1 + 2**-2, 128, float('Inf')], dtype=np.float32)
exponent_bits = 4
mantissa_bits = 2
self._assertOpOutputMatchesExpected(
    lambda x: xla.reduce_precision(x, exponent_bits, mantissa_bits),
    args=(arg,),
    expected=expected,
    equality_fn=self.assertAllEqual)

arg = np.array([4], dtype=np.float32)
expected = np.array([4], dtype=np.float32)
# Test passing numbers that cannot fit in a 32-bit integer.
exponent_bits = 2**33
mantissa_bits = 2**33
self._assertOpOutputMatchesExpected(
    lambda x: xla.reduce_precision(x, exponent_bits, mantissa_bits),
    args=(arg,),
    expected=expected,
    equality_fn=self.assertAllEqual)
