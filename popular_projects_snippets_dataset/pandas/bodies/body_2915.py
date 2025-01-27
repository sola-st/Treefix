# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
# GH#26825
dti = date_range("2016-04-05 04:30", periods=3, tz="UTC")
dti2 = dti.tz_convert("US/Pacific")

# mixed all-tzaware dtypes
df2 = DataFrame([dti, dti2])
assert (df2.dtypes == object).all()
res2 = df2.T
assert (res2.dtypes == [dti.dtype, dti2.dtype]).all()
