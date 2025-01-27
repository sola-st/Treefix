# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
expected = np.linspace(start, end, num, dtype=np.float32)
result = self._testTernary(
    math_ops.linspace,
    np.float32(start),
    np.float32(end),
    np.int32(num),
    expected)
# According to linspace spec, start has to be the first element and end has
# to be last element.
self.assertEqual(result[-1], expected[-1])
self.assertEqual(result[0], expected[0])
