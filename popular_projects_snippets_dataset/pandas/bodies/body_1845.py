# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

# make sure that we are setting the binner
# on these attributes
rng = date_range("1/1/2012", periods=100, freq="S")
ts = Series(np.arange(len(rng)), index=rng)
rs = ts.resample("30s")

# before use
getattr(rs, attr)

# after grouper is initialized is ok
rs.mean()
getattr(rs, attr)
