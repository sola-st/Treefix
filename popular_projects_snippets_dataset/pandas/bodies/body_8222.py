# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# we only preserve freq in unambiguous cases

# if localized to US/Eastern, this crosses a DST transition
dti = date_range("2014-03-08 23:00", "2014-03-09 09:00", freq="H")
assert dti.freq == "H"

result = dti.tz_localize(None)  # no-op
assert result.freq == "H"

result = dti.tz_localize("UTC")  # unambiguous freq preservation
assert result.freq == "H"

result = dti.tz_localize("US/Eastern", nonexistent="shift_forward")
assert result.freq is None
assert result.inferred_freq is None  # i.e. we are not _too_ strict here

# Case where we _can_ keep freq because we're length==1
dti2 = dti[:1]
result = dti2.tz_localize("US/Eastern")
assert result.freq == "H"
