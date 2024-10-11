# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
series = Series([data])

msg = "bool cannot act on a non-boolean single element Series"
with pytest.raises(ValueError, match=msg):
    series.bool()
