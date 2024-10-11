# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
mi = MultiIndex.from_product([list("ab"), range(3)], names=["first", "second"])
msg = "Must pass both levels and codes"
with pytest.raises(TypeError, match=msg):
    eval(repr(mi))
