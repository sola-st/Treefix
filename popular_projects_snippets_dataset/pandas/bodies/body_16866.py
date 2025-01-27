# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_get_dummies.py
result = get_dummies(df, prefix_sep="..", sparse=sparse)
expected = DataFrame(
    {
        "C": [1, 2, 3],
        "A..a": [True, False, True],
        "A..b": [False, True, False],
        "B..b": [True, True, False],
        "B..c": [False, False, True],
    },
)
expected[["C"]] = df[["C"]]
expected = expected[["C", "A..a", "A..b", "B..b", "B..c"]]
if sparse:
    cols = ["A..a", "A..b", "B..b", "B..c"]
    expected[cols] = expected[cols].astype(SparseDtype("bool", 0))

tm.assert_frame_equal(result, expected)

result = get_dummies(df, prefix_sep=["..", "__"], sparse=sparse)
expected = expected.rename(columns={"B..b": "B__b", "B..c": "B__c"})
tm.assert_frame_equal(result, expected)

result = get_dummies(df, prefix_sep={"A": "..", "B": "__"}, sparse=sparse)
tm.assert_frame_equal(result, expected)
