# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
# GH#26825
dti = date_range("2016-04-05 04:30", periods=3, tz="UTC")

df = DataFrame(dti)
assert (df.dtypes == dti.dtype).all()
res = df.T
assert (res.dtypes == dti.dtype).all()
