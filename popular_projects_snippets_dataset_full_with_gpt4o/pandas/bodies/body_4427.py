# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame({"a": np.random.randn(10), "b": True})
exp = DataFrame({"a": df["a"].values, "b": [True] * 10})

tm.assert_frame_equal(df, exp)
with pytest.raises(ValueError, match="must pass an index"):
    DataFrame({"a": False, "b": True})
