# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 17440
index = pd.MultiIndex.from_tuples(
    [("first", "second"), ("first", "third")], names=["baz", "foobar"]
)
df = DataFrame({"foo": [0, 1], "bar": [2, 3]}, index=index)
result = melt(df, ignore_index=False)

expected_index = pd.MultiIndex.from_tuples(
    [("first", "second"), ("first", "third")] * 2, names=["baz", "foobar"]
)
expected = DataFrame(
    {"variable": ["foo"] * 2 + ["bar"] * 2, "value": [0, 1, 2, 3]},
    index=expected_index,
)

tm.assert_frame_equal(result, expected)
