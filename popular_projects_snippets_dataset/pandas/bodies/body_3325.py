# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
df = DataFrame(data)
with pytest.raises(TypeError, match="'<' not supported between instances of"):
    df.rank()
result = df.rank(numeric_only=True)
tm.assert_frame_equal(result, expected)
