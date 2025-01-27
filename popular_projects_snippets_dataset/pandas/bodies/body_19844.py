# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
# calculate the actual result
carg = carg.astype(object, copy=False)
parsed = parsing.try_parse_year_month_day(
    carg / 10000, carg / 100 % 100, carg % 100
)
exit(tslib.array_to_datetime(parsed, errors=errors)[0])
