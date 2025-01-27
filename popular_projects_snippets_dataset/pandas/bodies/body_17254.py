# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
# multiple bool are still an error
series = Series([data])

msg = "The truth value of a Series is ambiguous"
with pytest.raises(ValueError, match=msg):
    bool(series)
with pytest.raises(ValueError, match=msg):
    series.bool()
