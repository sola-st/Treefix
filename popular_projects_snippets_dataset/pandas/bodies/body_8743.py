# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d

value = NaT.value
msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    # require NaT, not iNaT, as it could be confused with an integer
    arr.take([-1, 1], allow_fill=True, fill_value=value)

value = np.timedelta64("NaT", "ns")
with pytest.raises(TypeError, match=msg):
    # require appropriate-dtype if we have a NA value
    arr.take([-1, 1], allow_fill=True, fill_value=value)
