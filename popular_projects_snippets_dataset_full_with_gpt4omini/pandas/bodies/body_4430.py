# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# used to be in test_matrix.py
arr = np.random.randn(10)
dm = DataFrame(arr, columns=["A"], index=np.arange(10))
assert dm.values.ndim == 2

arr = np.random.randn(0)
dm = DataFrame(arr)
assert dm.values.ndim == 2
assert dm.values.ndim == 2

# no data specified
dm = DataFrame(columns=["A", "B"], index=np.arange(10))
assert dm.values.shape == (10, 2)

dm = DataFrame(columns=["A", "B"])
assert dm.values.shape == (0, 2)

dm = DataFrame(index=np.arange(10))
assert dm.values.shape == (10, 0)

# can't cast
mat = np.array(["foo", "bar"], dtype=object).reshape(2, 1)
msg = "could not convert string to float: 'foo'"
with pytest.raises(ValueError, match=msg):
    DataFrame(mat, index=[0, 1], columns=[0], dtype=float)

dm = DataFrame(DataFrame(float_frame._series))
tm.assert_frame_equal(dm, float_frame)

# int cast
dm = DataFrame(
    {"A": np.ones(10, dtype=int), "B": np.ones(10, dtype=np.float64)},
    index=np.arange(10),
)

assert len(dm.columns) == 2
assert dm.values.dtype == np.float64
