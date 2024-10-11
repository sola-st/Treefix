# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 14715
df = DataFrame({"date": date_range("1/1/2011", periods=365, freq="D")})
df.iloc[-1] = pd.NaT
grouper = Grouper(key="date", freq="AS")

# Grouper in a list grouping
result = df.groupby([grouper])
expected = {Timestamp("2011-01-01"): Index(list(range(364)))}
tm.assert_dict_equal(result.groups, expected)

# Test case without a list
result = df.groupby(grouper)
expected = {Timestamp("2011-01-01"): 365}
tm.assert_dict_equal(result.groups, expected)
