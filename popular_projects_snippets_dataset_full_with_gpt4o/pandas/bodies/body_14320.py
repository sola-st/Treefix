# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# GH 20594

dtype = pd.DatetimeTZDtype(tz=tz_aware_fixture)

obj = Series(dtype=dtype, name="A")
if frame_or_series is DataFrame:
    obj = obj.to_frame()

with ensure_clean_store(setup_path) as store:
    store["obj"] = obj
    result = store["obj"]
    tm.assert_equal(result, obj)
