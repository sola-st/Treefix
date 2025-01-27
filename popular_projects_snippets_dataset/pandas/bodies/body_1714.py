# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
b = Grouper(freq=Minute(5), closed="right", label="right")
dti = index.as_unit(unit)
df = DataFrame(np.random.rand(len(dti), 10), index=dti, dtype="float64")
r = df.groupby(b).agg(np.sum)

assert len(r.columns) == 10
assert len(r.index) == 2593
