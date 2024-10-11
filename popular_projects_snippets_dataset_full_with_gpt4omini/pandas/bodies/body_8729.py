# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# different timezones
arr = arr1d

if arr.tz is None:
    other = arr.tz_localize("UTC")
else:
    other = arr.tz_localize(None)

with pytest.raises(ValueError, match="to_concat must have the same"):
    arr._concat_same_type([arr, other])
