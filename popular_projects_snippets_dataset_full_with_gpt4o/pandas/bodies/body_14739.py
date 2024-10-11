# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 9012
# period-array conversions
df = DataFrame(
    np.random.rand(21, 2),
    index=bdate_range(datetime(2000, 1, 1), datetime(2000, 1, 31)),
    columns=["a", "b"],
)

df.plot()
self.plt.axhline(y=0)
tm.close()
