# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
frame = DataFrame({"a": np.random.randint(0, 5, 50), "b": ["foo", "bar"] * 25})

with pytest.raises(TypeError, match="Cannot use numeric_only=True"):
    frame.groupby("a")["b"].mean(numeric_only=True)

with pytest.raises(TypeError, match="Could not convert (foo|bar)*"):
    frame.groupby("a")["b"].mean()

frame = DataFrame({"a": np.random.randint(0, 5, 50), "b": ["foo", "bar"] * 25})

with pytest.raises(TypeError, match="Could not convert"):
    frame[["b"]].groupby(frame["a"]).mean()
result = frame[["b"]].groupby(frame["a"]).mean(numeric_only=True)
expected = DataFrame(
    [], index=frame["a"].sort_values().drop_duplicates(), columns=[]
)
tm.assert_frame_equal(result, expected)
