# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
msg = r"percentiles should all be in the interval \[0,1\]"
with pytest.raises(ValueError, match=msg):
    fmt.format_percentiles(percentiles)
