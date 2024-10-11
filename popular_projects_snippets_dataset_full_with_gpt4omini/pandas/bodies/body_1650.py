# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#33964
index = pd.period_range(start="2000", periods=20, freq="B")
series = Series(range(20), index=index)
assert series.loc["2000-01-14"] == 9
