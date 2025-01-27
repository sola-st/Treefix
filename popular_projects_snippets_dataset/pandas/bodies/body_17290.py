# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
idx = pd.MultiIndex.from_product([["A"], ["a", "b", "a", "b", "c"]])
result = idx._format_duplicate_message()
expected = pd.DataFrame(
    {"positions": [[0, 2], [1, 3]]},
    index=pd.MultiIndex.from_product([["A"], ["a", "b"]]),
)
tm.assert_frame_equal(result, expected)
