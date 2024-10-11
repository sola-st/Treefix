# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
rng = bdate_range(START, END, freq=freq)
with pytest.raises(ValueError, match="Multi-dimensional indexing"):
    # GH#30588 multi-dimensional indexing deprecated
    rng[:, None]
