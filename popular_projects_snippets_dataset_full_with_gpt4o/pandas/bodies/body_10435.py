# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# Checks that groupby-transform, when grouping by both a categorical
# and a non-categorical key, doesn't try to expand the output to include
# non-observed categories but instead matches the input shape.
# GH 32494
df_with_categorical = DataFrame(
    {
        "A": Categorical(["a", "b", "a"], categories=["a", "b", "c"]),
        "B": [1, 2, 3],
        "C": ["a", "b", "a"],
    }
)
df_without_categorical = DataFrame(
    {"A": ["a", "b", "a"], "B": [1, 2, 3], "C": ["a", "b", "a"]}
)

# DataFrame case
result = df_with_categorical.groupby(["A", "C"], observed=observed).transform("sum")
expected = df_without_categorical.groupby(["A", "C"]).transform("sum")
tm.assert_frame_equal(result, expected)
expected_explicit = DataFrame({"B": [4, 2, 4]})
tm.assert_frame_equal(result, expected_explicit)

# Series case
result = df_with_categorical.groupby(["A", "C"], observed=observed)["B"].transform(
    "sum"
)
expected = df_without_categorical.groupby(["A", "C"])["B"].transform("sum")
tm.assert_series_equal(result, expected)
expected_explicit = Series([4, 2, 4], name="B")
tm.assert_series_equal(result, expected_explicit)
