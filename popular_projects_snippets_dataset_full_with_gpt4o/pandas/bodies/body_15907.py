# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
#  GH 20925

# KeyError raised for series index when passed level name is missing
s = Series(range(4))
with pytest.raises(KeyError, match="does not match index name"):
    s.reset_index("wrong", drop=True)
with pytest.raises(KeyError, match="does not match index name"):
    s.reset_index("wrong")

# KeyError raised for series when level to be dropped is missing
s = Series(range(4), index=MultiIndex.from_product([[1, 2]] * 2))
with pytest.raises(KeyError, match="not found"):
    s.reset_index("wrong", drop=True)
