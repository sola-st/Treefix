# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
# test for fill value during upsampling, related to issue 3715

# setup
rng = date_range("1/1/2016", periods=10, freq="2S")
# Explicit cast to 'float' to avoid implicit cast when setting None
ts = Series(np.arange(len(rng)), index=rng, dtype="float")
df = DataFrame({"one": ts})

# insert pre-existing missing value
df.loc["2016-01-01 00:00:08", "one"] = None

actual_df = df.asfreq(freq="1S", fill_value=9.0)
expected_df = df.asfreq(freq="1S").fillna(9.0)
expected_df.loc["2016-01-01 00:00:08", "one"] = None
tm.assert_frame_equal(expected_df, actual_df)

expected_series = ts.asfreq(freq="1S").fillna(9.0)
actual_series = ts.asfreq(freq="1S", fill_value=9.0)
tm.assert_series_equal(expected_series, actual_series)
