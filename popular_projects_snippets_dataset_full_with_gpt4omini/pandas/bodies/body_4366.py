# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# as of 2.0, we raise if we can't respect "dtype", previously we
#  silently ignored
msg = "could not convert string to float"
with pytest.raises(ValueError, match=msg):
    DataFrame({"a": ["a", "b", "c"]}, dtype=np.float64)

# GH 3010, constructing with odd arrays
df = DataFrame(np.ones((4, 2)))

# this is ok
df["foo"] = np.ones((4, 2)).tolist()

# this is not ok
msg = "Expected a 1D array, got an array with shape \\(4, 2\\)"
with pytest.raises(ValueError, match=msg):
    df["test"] = np.ones((4, 2))

# this is ok
df["foo2"] = np.ones((4, 2)).tolist()
