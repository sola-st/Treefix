# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
# TODO: should this raise TypeError
values = Series(["fooBAD__barBAD", np.nan, "foo"], dtype=any_string_dtype)
with pytest.raises(ValueError, match="expand must be True or False"):
    values.str.extract(".*(BAD[_]+).*(BAD)", expand=None)
