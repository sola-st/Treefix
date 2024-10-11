# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
frame = DataFrame(
    {
        "a": np.random.randint(0, 5, 50),
        "b": ["foo", "bar"] * 25,
        "dates": pd.date_range("now", periods=50, freq="T"),
    }
)
with pytest.raises(TypeError, match="Cannot use numeric_only=True"):
    frame.groupby("b").dates.mean(numeric_only=True)
