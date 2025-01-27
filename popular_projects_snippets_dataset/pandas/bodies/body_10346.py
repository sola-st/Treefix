# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# Test for error on invalid argument

with pytest.raises(TypeError, match="Invalid index"):
    slice_test_grouped.nth(3.14)
