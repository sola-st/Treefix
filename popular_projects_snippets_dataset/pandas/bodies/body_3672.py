# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
# GH#4211
df = DataFrame(
    {
        "vals": [1, 2, 3, 4],
        "ids": ["a", "b", "f", "n"],
        "ids2": ["a", "n", "c", "n"],
    },
    index=["foo", "bar", "baz", "qux"],
)
other = ["a", "b", "c"]

result = df.isin(other)
expected = DataFrame([df.loc[s].isin(other) for s in df.index])
tm.assert_frame_equal(result, expected)
