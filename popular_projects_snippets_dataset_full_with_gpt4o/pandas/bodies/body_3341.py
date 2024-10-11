# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH-39338
df = DataFrame(
    {
        "col1": ["1,000", "a", "3"],
        "col2": ["a", "", "b"],
        "col3": ["a", "b", "c"],
    }
)
result = df.replace(regex=to_replace)
expected = DataFrame(
    {
        "col1": ["1000", "a", "3"],
        "col2": ["a", np.nan, "b"],
        "col3": ["a", "b", "c"],
    }
)
tm.assert_frame_equal(result, expected)
