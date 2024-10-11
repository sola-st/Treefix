# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
# MultiIndex has mixed dtype, but not allow to use accessor
idx = MultiIndex.from_tuples([("a", "b"), ("a", "b")])
assert idx.inferred_type == "mixed"

msg = "Can only use .str accessor with Index, not MultiIndex"
with pytest.raises(AttributeError, match=msg):
    idx.str
