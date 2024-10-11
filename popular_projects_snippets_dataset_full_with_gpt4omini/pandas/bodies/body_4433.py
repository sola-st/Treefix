# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH #484
df = DataFrame(data=[[1, "a"], [2, "b"]], columns=["num", "str"])
assert is_integer_dtype(df["num"])
assert df["str"].dtype == np.object_

# GH 4851
# list of 0-dim ndarrays
expected = DataFrame({0: np.arange(10)})
data = [np.array(x) for x in range(10)]
result = DataFrame(data)
tm.assert_frame_equal(result, expected)
