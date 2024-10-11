# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d
dti = self.index_cls(arr1d)

now = fixed_now_ts.tz_localize(dti.tz)
result = arr.take([-1, 1], allow_fill=True, fill_value=now)
assert result[0] == now

msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    # fill_value Timedelta invalid
    arr.take([-1, 1], allow_fill=True, fill_value=now - now)

with pytest.raises(TypeError, match=msg):
    # fill_value Period invalid
    arr.take([-1, 1], allow_fill=True, fill_value=Period("2014Q1"))

tz = None if dti.tz is not None else "US/Eastern"
now = fixed_now_ts.tz_localize(tz)
msg = "Cannot compare tz-naive and tz-aware datetime-like objects"
with pytest.raises(TypeError, match=msg):
    # Timestamp with mismatched tz-awareness
    arr.take([-1, 1], allow_fill=True, fill_value=now)

value = NaT.value
msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    # require NaT, not iNaT, as it could be confused with an integer
    arr.take([-1, 1], allow_fill=True, fill_value=value)

value = np.timedelta64("NaT", "ns")
with pytest.raises(TypeError, match=msg):
    # require appropriate-dtype if we have a NA value
    arr.take([-1, 1], allow_fill=True, fill_value=value)

if arr.tz is not None:
    # GH#37356
    # Assuming here that arr1d fixture does not include Australia/Melbourne
    value = fixed_now_ts.tz_localize("Australia/Melbourne")
    result = arr.take([-1, 1], allow_fill=True, fill_value=value)

    expected = arr.take(
        [-1, 1],
        allow_fill=True,
        fill_value=value.tz_convert(arr.dtype.tz),
    )
    tm.assert_equal(result, expected)
