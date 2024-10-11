# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#26825 2D object array of tzaware timestamps should not raise
dti = date_range("2016-04-05 04:30", periods=3, tz="UTC")
data = dti._data.astype(object).reshape(1, -1)
df = DataFrame(data)
assert df.shape == (1, 3)
assert (df.dtypes == dti.dtype).all()
assert (df == dti).all().all()
