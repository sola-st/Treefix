# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GB 6608
s1 = Series(
    [1, 2, 3],
    index=[
        datetime(1995, 12, 31),
        datetime(2000, 12, 31),
        datetime(2005, 12, 31),
    ],
)
s2 = Series(
    [1, 2, 3],
    index=[
        datetime(1997, 12, 31),
        datetime(2003, 12, 31),
        datetime(2008, 12, 31),
    ],
)

# plot first series, then add the second series to those axes,
# then try adding the first series again
_, ax = self.plt.subplots()
s1.plot(ax=ax)
s2.plot(ax=ax)
s1.plot(ax=ax)
