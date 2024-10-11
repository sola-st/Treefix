# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_index_as_string.py
if "B" not in key_strs or "outer" in frame.columns:
    with pytest.raises(TypeError, match="Could not convert"):
        frame.groupby(key_strs).mean()
    result = frame.groupby(key_strs).mean(numeric_only=True)

    with pytest.raises(TypeError, match="Could not convert"):
        frame.groupby(groupers).mean()
    expected = frame.groupby(groupers).mean(numeric_only=True)
else:
    result = frame.groupby(key_strs).mean()
    expected = frame.groupby(groupers).mean()
tm.assert_frame_equal(result, expected)
