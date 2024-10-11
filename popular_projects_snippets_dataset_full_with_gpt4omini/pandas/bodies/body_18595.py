# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parse_iso8601.py
msg = f'Error parsing datetime string "{date_str}"'

with pytest.raises(ValueError, match=msg):
    tslib._test_parse_iso8601(date_str)
