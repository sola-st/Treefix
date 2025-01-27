# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
from pandas.io.json import dumps

dti = pd.date_range("2013-01-01 05:00:00", periods=2)

exp = '["2013-01-01T05:00:00.000","2013-01-02T05:00:00.000"]'
dfexp = '{"DT":{"0":"2013-01-01T05:00:00.000","1":"2013-01-02T05:00:00.000"}}'

# Ensure datetimes in object array are serialized correctly
# in addition to the normal DTI case
assert dumps(dti, iso_dates=True) == exp
assert dumps(dti.astype(object), iso_dates=True) == exp
df = DataFrame({"DT": dti})
result = dumps(df, iso_dates=True)
assert result == dfexp
assert dumps(df.astype({"DT": object}), iso_dates=True)
