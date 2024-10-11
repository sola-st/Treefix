# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_cov_corr.py
# GH#34611
np_array1 = np.random.rand(10)
np_array2 = np.random.rand(10)

s1 = Series(np_array1)
s2 = Series(np_array2)

result = s1.cov(s2, ddof=test_ddof)
expected = np.cov(np_array1, np_array2, ddof=test_ddof)[0][1]
assert math.isclose(expected, result)
