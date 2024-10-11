# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
dti = date_range(start="1/1/2001", end="6/1/2001", freq="D")._with_freq(None)
d1 = DataFrame({"v": np.random.rand(len(dti))}, index=dti)
d2 = d1.reset_index()
assert d2.dtypes[0] == np.dtype("M8[ns]")
d3 = d2.set_index("index")
tm.assert_frame_equal(d1, d3, check_names=False)

# GH#2329
stamp = datetime(2012, 11, 22)
df = DataFrame([[stamp, 12.1]], columns=["Date", "Value"])
df = df.set_index("Date")

assert df.index[0] == stamp
assert df.reset_index()["Date"][0] == stamp
