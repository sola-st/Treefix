# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH42618
df = DataFrame(data=[range(len(columns))], columns=columns)
dfg = df.groupby(columns[:-1])

result = dfg[columns[-1]].value_counts()
expected = df.value_counts().rename(columns[-1])

tm.assert_series_equal(result, expected)
