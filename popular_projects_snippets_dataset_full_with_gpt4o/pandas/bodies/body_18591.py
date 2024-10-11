# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timedeltas.py
# check we raise, not segfault
values = np.arange(5)

msg = "'values' must have object dtype"
with pytest.raises(TypeError, match=msg):
    array_to_timedelta64(values)
