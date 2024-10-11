# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
a = pd.array([1, 2, np.nan])
result = np.modf(a)
expected = np.modf(a.to_numpy(na_value=np.nan, dtype="float"))
expected = (pd.array(expected[0]), pd.array(expected[1]))

assert isinstance(result, tuple)
assert len(result) == 2

for x, y in zip(result, expected):
    tm.assert_extension_array_equal(x, y)
