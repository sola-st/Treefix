# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
df = tm.makeTimeDataFrame()
df.index = df.index.as_unit(unit)

b = Grouper(freq="M")
g = df.groupby(b)

# check all cython functions work
g._cython_agg_general(f, alt=None, numeric_only=True)
