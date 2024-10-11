# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# gh-46634
cat_series = Series(["b", "b", "b", "d"], dtype="category")
df = DataFrame(
    {
        "id": Series([5, 4, 3, 2], dtype="float64"),
        "col": cat_series,
    }
)
result = df.replace({3: None})

expected = DataFrame(
    {
        "id": Series([5.0, 4.0, None, 2.0], dtype="object"),
        "col": cat_series,
    }
)
tm.assert_frame_equal(result, expected)
