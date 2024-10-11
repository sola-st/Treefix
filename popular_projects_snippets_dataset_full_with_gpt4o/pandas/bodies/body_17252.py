# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
# single item nan to raise
series = Series([data])

msg = "The truth value of a Series is ambiguous"
with pytest.raises(ValueError, match=msg):
    bool(series)
