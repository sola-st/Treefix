# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 15273
df = DataFrame(
    True,
    index=pd.date_range("2017-01-20", "2017-01-23"),
    columns=["foo", "bar"],
).stack()
result = df.to_json()
expected = (
    "{\"(Timestamp('2017-01-20 00:00:00'), 'foo')\":true,"
    "\"(Timestamp('2017-01-20 00:00:00'), 'bar')\":true,"
    "\"(Timestamp('2017-01-21 00:00:00'), 'foo')\":true,"
    "\"(Timestamp('2017-01-21 00:00:00'), 'bar')\":true,"
    "\"(Timestamp('2017-01-22 00:00:00'), 'foo')\":true,"
    "\"(Timestamp('2017-01-22 00:00:00'), 'bar')\":true,"
    "\"(Timestamp('2017-01-23 00:00:00'), 'foo')\":true,"
    "\"(Timestamp('2017-01-23 00:00:00'), 'bar')\":true}"
)
assert result == expected
