# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH#46672
df = DataFrame(
    {
        "a": ["one", "two", None, "three"],
        "b": ["one", None, "two", "three"],
    },
    dtype="category",
)
expected = df.copy()

result = df.replace(to_replace=[".", "def"], value=["_", None])
tm.assert_frame_equal(result, expected)
