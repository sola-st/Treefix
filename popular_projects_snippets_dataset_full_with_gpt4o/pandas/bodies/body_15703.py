# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_add_prefix_suffix.py
with pytest.raises(ValueError, match="No axis named 1 for object type Series"):
    string_series.add_prefix("foo#", axis=1)

with pytest.raises(ValueError, match="No axis named 1 for object type Series"):
    string_series.add_suffix("foo#", axis=1)
