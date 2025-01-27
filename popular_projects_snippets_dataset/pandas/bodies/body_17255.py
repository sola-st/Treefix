# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
# single non-bool are an error
series = Series([data])

msg = "The truth value of a Series is ambiguous"
with pytest.raises(ValueError, match=msg):
    bool(series)

msg = "bool cannot act on a non-boolean single element Series"
with pytest.raises(ValueError, match=msg):
    series.bool()
