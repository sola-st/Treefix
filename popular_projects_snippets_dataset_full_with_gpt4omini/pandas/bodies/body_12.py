# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
s = Series(range(6), dtype="int64", name="series")
msg = "nested renamer is not supported"
with pytest.raises(SpecificationError, match=msg):
    s.agg(renamer)
