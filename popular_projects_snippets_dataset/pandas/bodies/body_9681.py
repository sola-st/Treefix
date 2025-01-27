# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_constructors.py
# GH#44507
td = pd.NaT.to_numpy("m8[ns]")

dtype = pd.period_range("2005-01-01", periods=3, freq="D").dtype

arr = np.array([None], dtype=object)
arr[0] = td

msg = "Value must be Period, string, integer, or datetime"
with pytest.raises(ValueError, match=msg):
    PeriodArray._from_sequence(arr, dtype=dtype)

with pytest.raises(ValueError, match=msg):
    pd.PeriodIndex(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.Index(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.array(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.Series(arr, dtype=dtype)
with pytest.raises(ValueError, match=msg):
    pd.DataFrame(arr, dtype=dtype)
