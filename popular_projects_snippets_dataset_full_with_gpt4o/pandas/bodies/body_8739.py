# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
tdi = timedelta_index
arr = TimedeltaArray(tdi)

td1 = pd.Timedelta(days=1)
result = arr.take([-1, 1], allow_fill=True, fill_value=td1)
assert result[0] == td1

value = fixed_now_ts
msg = f"value should be a '{arr._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    # fill_value Timestamp invalid
    arr.take([0, 1], allow_fill=True, fill_value=value)

value = fixed_now_ts.to_period("D")
with pytest.raises(TypeError, match=msg):
    # fill_value Period invalid
    arr.take([0, 1], allow_fill=True, fill_value=value)

value = np.datetime64("NaT", "ns")
with pytest.raises(TypeError, match=msg):
    # require appropriate-dtype if we have a NA value
    arr.take([-1, 1], allow_fill=True, fill_value=value)
