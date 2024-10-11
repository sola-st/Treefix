# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# see gh-11682: Timezone info lost when broadcasting
# scalar datetime to DataFrame

df = DataFrame({"a": [1], "b": [datetime.now(pytz.utc)]})
assert df["b"][0].tzinfo == pytz.utc
df = DataFrame({"a": [1, 2, 3]})
df["b"] = datetime.now(pytz.utc)
assert df["b"][0].tzinfo == pytz.utc
