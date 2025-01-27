# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 34832
df = DataFrame(index=[0, 1], columns=["a", "b"], data=data)

assert df["a"].dtype == dtype
assert df["b"].dtype == dtype

arr = pd.array([data] * 2, dtype=dtype)
expected = DataFrame({"a": arr, "b": arr})

tm.assert_frame_equal(df, expected)
