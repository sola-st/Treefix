# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# see GH#19399
df = DataFrame([1, 2], index=[2**63 - 1, 2**63])
result = df.loc[val]

expected.name = val
tm.assert_series_equal(result, expected)
