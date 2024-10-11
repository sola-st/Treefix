# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
"""Length 2 array with [NA, Valid]"""
arr = dtype.construct_array_type()._from_sequence([pd.NA, "A"])
exit(split_array(arr) if chunked else arr)
