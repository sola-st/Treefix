# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timezones.py
eastern, localize = request.param

start_naive = datetime(2001, 1, 1)
end_naive = datetime(2009, 1, 1)

start = localize(eastern, start_naive)
end = localize(eastern, end_naive)

exit((eastern, localize, start, end, start_naive, end_naive))
