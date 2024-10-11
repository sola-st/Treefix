# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
values = date_range("2011-01-01", "2011-01-02", freq="H").tz_localize("Asia/Tokyo")
s = Series(values, name="XX")
with pytest.raises(NotImplementedError, match=tm.EMPTY_STRING_PATTERN):
    s.map(lambda x: x, na_action="ignore")
