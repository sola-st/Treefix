# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
for dtype in self.float_types:
    if dtype != np.float16:
        self._assertOpOutputMatchesExpected(
            lambda x: math_ops.sigmoid(x) / math_ops.log1p(math_ops.exp(x)),
            np.array([-40, 40], dtype=dtype),
            expected=np.array([1.0, 0.025], dtype=dtype))
