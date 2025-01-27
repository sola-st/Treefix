# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_parse_iso8601.py
date_str = "2001-01-01 12-34-56"
msg = f'Timezone hours offset out of range in datetime string "{date_str}"'

with pytest.raises(ValueError, match=msg):
    tslib._test_parse_iso8601(date_str)
