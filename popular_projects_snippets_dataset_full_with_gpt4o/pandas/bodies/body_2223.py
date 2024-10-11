# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# OK
# 2.5.1 10-11-12   [dayfirst=0, yearfirst=0] -> 2012-10-11 00:00:00
# 2.5.2 10-11-12   [dayfirst=0, yearfirst=1] -> 2012-10-11 00:00:00
# 2.5.3 10-11-12   [dayfirst=0, yearfirst=0] -> 2012-10-11 00:00:00

# OK
# 2.5.1 10-11-12   [dayfirst=0, yearfirst=1] -> 2010-11-12 00:00:00
# 2.5.2 10-11-12   [dayfirst=0, yearfirst=1] -> 2010-11-12 00:00:00
# 2.5.3 10-11-12   [dayfirst=0, yearfirst=1] -> 2010-11-12 00:00:00

# bug fix in 2.5.2
# 2.5.1 10-11-12   [dayfirst=1, yearfirst=1] -> 2010-11-12 00:00:00
# 2.5.2 10-11-12   [dayfirst=1, yearfirst=1] -> 2010-12-11 00:00:00
# 2.5.3 10-11-12   [dayfirst=1, yearfirst=1] -> 2010-12-11 00:00:00

# OK
# 2.5.1 10-11-12   [dayfirst=1, yearfirst=0] -> 2012-11-10 00:00:00
# 2.5.2 10-11-12   [dayfirst=1, yearfirst=0] -> 2012-11-10 00:00:00
# 2.5.3 10-11-12   [dayfirst=1, yearfirst=0] -> 2012-11-10 00:00:00

# OK
# 2.5.1 20/12/21   [dayfirst=0, yearfirst=0] -> 2021-12-20 00:00:00
# 2.5.2 20/12/21   [dayfirst=0, yearfirst=0] -> 2021-12-20 00:00:00
# 2.5.3 20/12/21   [dayfirst=0, yearfirst=0] -> 2021-12-20 00:00:00

# OK
# 2.5.1 20/12/21   [dayfirst=0, yearfirst=1] -> 2020-12-21 00:00:00
# 2.5.2 20/12/21   [dayfirst=0, yearfirst=1] -> 2020-12-21 00:00:00
# 2.5.3 20/12/21   [dayfirst=0, yearfirst=1] -> 2020-12-21 00:00:00

# revert of bug in 2.5.2
# 2.5.1 20/12/21   [dayfirst=1, yearfirst=1] -> 2020-12-21 00:00:00
# 2.5.2 20/12/21   [dayfirst=1, yearfirst=1] -> month must be in 1..12
# 2.5.3 20/12/21   [dayfirst=1, yearfirst=1] -> 2020-12-21 00:00:00

# OK
# 2.5.1 20/12/21   [dayfirst=1, yearfirst=0] -> 2021-12-20 00:00:00
# 2.5.2 20/12/21   [dayfirst=1, yearfirst=0] -> 2021-12-20 00:00:00
# 2.5.3 20/12/21   [dayfirst=1, yearfirst=0] -> 2021-12-20 00:00:00

# str : dayfirst, yearfirst, expected

# compare with dateutil result
dateutil_result = parse(date_str, dayfirst=dayfirst, yearfirst=yearfirst)
assert dateutil_result == expected

result1, _ = parsing.parse_datetime_string_with_reso(
    date_str, dayfirst=dayfirst, yearfirst=yearfirst
)

# we don't support dayfirst/yearfirst here:
if not dayfirst and not yearfirst:
    result2 = Timestamp(date_str)
    assert result2 == expected

with tm.assert_produces_warning(UserWarning, match="Could not infer format"):
    result3 = to_datetime(
        date_str, dayfirst=dayfirst, yearfirst=yearfirst, cache=cache
    )

result4 = DatetimeIndex([date_str], dayfirst=dayfirst, yearfirst=yearfirst)[0]

assert result1 == expected
assert result3 == expected
assert result4 == expected
