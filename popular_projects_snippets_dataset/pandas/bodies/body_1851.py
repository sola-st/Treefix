# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

# need to upsample here
rng = date_range("1/1/2012", periods=10, freq="2S")
ts = Series(np.arange(len(rng), dtype="int64"), index=rng)
r = ts.resample("s")

expected = r.ffill()
result = r.fillna(method="ffill")
tm.assert_series_equal(result, expected)

expected = r.bfill()
result = r.fillna(method="bfill")
tm.assert_series_equal(result, expected)

msg = (
    r"Invalid fill method\. Expecting pad \(ffill\), backfill "
    r"\(bfill\) or nearest\. Got 0"
)
with pytest.raises(ValueError, match=msg):
    r.fillna(0)
