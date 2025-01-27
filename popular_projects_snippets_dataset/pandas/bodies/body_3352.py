# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py

# to object block upcasting
df = DataFrame(
    {
        "A": Series([1.0, 2.0], dtype="float64"),
        "B": Series([0, 1], dtype="int64"),
    }
)
expected = DataFrame(
    {
        "A": Series([1, "foo"], dtype="object"),
        "B": Series([0, 1], dtype="int64"),
    }
)
result = df.replace(2, "foo")
tm.assert_frame_equal(result, expected)

expected = DataFrame(
    {
        "A": Series(["foo", "bar"], dtype="object"),
        "B": Series([0, "foo"], dtype="object"),
    }
)
result = df.replace([1, 2], ["foo", "bar"])
tm.assert_frame_equal(result, expected)
