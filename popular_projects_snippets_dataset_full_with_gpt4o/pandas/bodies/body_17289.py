# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
idx = pd.Index(["a", "b", "a", "b", "c"])
result = idx._format_duplicate_message()
expected = pd.DataFrame(
    {"positions": [[0, 2], [1, 3]]}, index=pd.Index(["a", "b"], name="label")
)
tm.assert_frame_equal(result, expected)
