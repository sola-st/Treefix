# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/31964
dti = pd.DatetimeIndex(["2016-06-26 14:27:26+00:00"])
df = DataFrame(index=pd.DatetimeIndex(["2016-07-04 14:00:59+00:00"]))
expected = DataFrame(index=dti)
result = df.reindex(dti, method="nearest")
tm.assert_frame_equal(result, expected)
