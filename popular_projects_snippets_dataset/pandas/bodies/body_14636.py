# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH 3490 - regular-timeseries with secondary y
index_1 = date_range(start="2000-01-01", periods=4, freq="D")
index_2 = date_range(start="2000-01-05", periods=4, freq="D")
s1 = Series(1, index=index_1)
s2 = Series(2, index=index_2)

_, ax = self.plt.subplots()
s1.plot(ax=ax)
left_before, right_before = ax.get_xlim()
s2.plot(secondary_y=True, ax=ax)
left_after, right_after = ax.get_xlim()

assert left_before >= left_after
assert right_before < right_after
