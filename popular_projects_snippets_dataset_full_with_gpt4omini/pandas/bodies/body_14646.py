# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# https://github.com/matplotlib/matplotlib/issues/11391
df = DataFrame(np.random.RandomState(0).rand(10, 2), columns=["x", "y"])
df["time"] = date_range("2018-01-01", periods=10, freq="D")
fig, ax = self.plt.subplots()
ax.scatter(x="time", y="y", data=df)
self.plt.draw()
label = ax.get_xticklabels()[0]
expected = "2018-01-01"
assert label.get_text() == expected
