# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# not sure what else to do here
series = float_frame["A"][::2]
float_frame["col5"] = series
assert "col5" in float_frame

assert len(series) == 15
assert len(float_frame) == 30

exp = np.ravel(np.column_stack((series.values, [np.nan] * 15)))
exp = Series(exp, index=float_frame.index, name="col5")
tm.assert_series_equal(float_frame["col5"], exp)

series = float_frame["A"]
float_frame["col6"] = series
tm.assert_series_equal(series, float_frame["col6"], check_names=False)

# set ndarray
arr = np.random.randn(len(float_frame))
float_frame["col9"] = arr
assert (float_frame["col9"] == arr).all()

float_frame["col7"] = 5
assert (float_frame["col7"] == 5).all()

float_frame["col0"] = 3.14
assert (float_frame["col0"] == 3.14).all()

float_frame["col8"] = "foo"
assert (float_frame["col8"] == "foo").all()

# this is partially a view (e.g. some blocks are view)
# so raise/warn
smaller = float_frame[:2]

msg = r"\nA value is trying to be set on a copy of a slice from a DataFrame"
if using_copy_on_write:
    # With CoW, adding a new column doesn't raise a warning
    smaller["col10"] = ["1", "2"]
else:
    with pytest.raises(SettingWithCopyError, match=msg):
        smaller["col10"] = ["1", "2"]

assert smaller["col10"].dtype == np.object_
assert (smaller["col10"] == ["1", "2"]).all()
