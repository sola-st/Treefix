# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ternary_ops_test.py
for dtype in self.numeric_types - self.complex_types:
    test_cases = [
        (np.array([2, 4, 5], dtype=dtype), dtype(7)),  #
        (dtype(1), np.array([2, 4, 5], dtype=dtype)),  #
        (np.array([-2, 7, 7], dtype=dtype), np.array([-2, 9, 8], dtype=dtype))
    ]
    x = np.array([-2, 10, 6], dtype=dtype)
    for lower, upper in test_cases:
        self._testTernary(
            gen_math_ops._clip_by_value,
            x,
            lower,
            upper,
            expected=np.minimum(np.maximum(x, lower), upper))
