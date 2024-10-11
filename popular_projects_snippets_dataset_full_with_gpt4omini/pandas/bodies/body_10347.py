# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# Test for error on negative slice step

with pytest.raises(ValueError, match="Invalid step"):
    slice_test_grouped.nth(slice(None, None, -1))
