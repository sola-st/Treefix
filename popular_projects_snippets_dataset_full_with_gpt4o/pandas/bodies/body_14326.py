# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
# GH 11926
periods = 10
dts = date_range("20151201", periods=periods, freq="D", tz="UTC")
mi = pd.MultiIndex.from_arrays([dts, range(periods)], names=["DATE", "NO"])
expected = DataFrame({"MYCOL": 0}, index=mi)

key = "mykey"
path = tmp_path / setup_path
with pd.HDFStore(path) as store:
    store.append(key, expected, format="table", append=True)
result = pd.read_hdf(path, key, where="DATE > 20151130")
tm.assert_frame_equal(result, expected)
