# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
for level in [10, index.nlevels, -(index.nlevels + 1)]:
    with pytest.raises(IndexError, match="Too many levels"):
        index.isin([], level=level)
