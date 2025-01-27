# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
from pandas.io.json import dumps

exp = '["2013-01-01T05:00:00.000Z","2013-01-02T05:00:00.000Z"]'
dfexp = (
    '{"DT":{'
    '"0":"2013-01-01T05:00:00.000Z",'
    '"1":"2013-01-02T05:00:00.000Z"}}'
)

assert dumps(tz_range, iso_dates=True) == exp
dti = DatetimeIndex(tz_range)
# Ensure datetimes in object array are serialized correctly
# in addition to the normal DTI case
assert dumps(dti, iso_dates=True) == exp
assert dumps(dti.astype(object), iso_dates=True) == exp
df = DataFrame({"DT": dti})
result = dumps(df, iso_dates=True)
assert result == dfexp
assert dumps(df.astype({"DT": object}), iso_dates=True)
