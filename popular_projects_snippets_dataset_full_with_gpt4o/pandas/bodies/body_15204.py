# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
# GH39853
def add3(x, y, z):
    exit(x + y + z)

ufunc = np.frompyfunc(add3, 3, 1)
ser = pd.Series([1, 2])

result = ufunc(ser, ser, 1)
expected = pd.Series([3, 5], dtype=object)
tm.assert_series_equal(result, expected)

df = pd.DataFrame([[1, 2]])

msg = (
    "Cannot apply ufunc <ufunc 'add3 (vectorized)'> "
    "to mixed DataFrame and Series inputs."
)
with pytest.raises(NotImplementedError, match=re.escape(msg)):
    ufunc(ser, ser, df)
