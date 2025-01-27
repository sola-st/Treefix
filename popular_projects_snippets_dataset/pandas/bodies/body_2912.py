# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
# GH#26825
dti = date_range("2016-04-05 04:30", periods=3, tz="UTC")

df3 = DataFrame({"A": dti, "B": dti})
assert (df3.dtypes == dti.dtype).all()
res3 = df3.T
assert (res3.dtypes == dti.dtype).all()
