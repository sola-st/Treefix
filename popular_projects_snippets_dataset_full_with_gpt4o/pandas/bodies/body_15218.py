# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_delitem.py
# empty
s = Series(dtype=object)

with pytest.raises(KeyError, match=r"^0$"):
    del s[0]
