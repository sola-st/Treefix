# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# TODO: a bunch of scattered tests check this deprecation is enforced.
#  de-duplicate/centralize them.
with pytest.raises(ValueError, match="Multi-dimensional indexing"):
    # GH#30588 multi-dimensional indexing deprecated
    index[None, :]
