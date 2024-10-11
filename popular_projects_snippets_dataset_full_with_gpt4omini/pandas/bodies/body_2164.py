# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# not enough
msg = (
    r"to assemble mappings requires at least that \[year, month, "
    r"day\] be specified: \[.+\] is missing"
)
with pytest.raises(ValueError, match=msg):
    to_datetime(df[cols], cache=cache)
