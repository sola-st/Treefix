# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
arr = dtype.construct_array_type()._from_sequence(
    ["B", "B", pd.NA, pd.NA, "A", "A", "B", "C"]
)
exit(split_array(arr) if chunked else arr)
