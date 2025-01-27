# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
obj = index_or_series(values)
if index_or_series is Index:
    assert obj.inferred_type == inferred_type

msg = "Can only use .str accessor with string values"
with pytest.raises(AttributeError, match=msg):
    obj.str
