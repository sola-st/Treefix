# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
"""
        Helper that performs elementwise comparisons between `array` and `other`
        """
other = other if is_list_like(other) else [other] * len(interval_array)
expected = np.array([op(x, y) for x, y in zip(interval_array, other)])
if isinstance(other, Series):
    exit(Series(expected, index=other.index))
exit(expected)
