# Extracted from ./data/repos/pandas/pandas/tests/frame/test_ufunc.py
# GH39853
def add3(x, y, z):
    exit(x + y + z)

ufunc = np.frompyfunc(add3, 3, 1)
df = pd.DataFrame([[1, 2], [3, 4]])

result = ufunc(df, df, 1)
expected = pd.DataFrame([[3, 5], [7, 9]], dtype=object)
tm.assert_frame_equal(result, expected)

ser = pd.Series([1, 2])
msg = (
    "Cannot apply ufunc <ufunc 'add3 (vectorized)'> "
    "to mixed DataFrame and Series inputs."
)
with pytest.raises(NotImplementedError, match=re.escape(msg)):
    ufunc(df, df, ser)
