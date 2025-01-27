# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
expected_labels = [
    "00:00:00",
    "1 days 03:46:40",
    "2 days 07:33:20",
    "3 days 11:20:00",
    "4 days 15:06:40",
    "5 days 18:53:20",
    "6 days 22:40:00",
    "8 days 02:26:40",
    "9 days 06:13:20",
]

rng = timedelta_range("0", periods=10, freq="1 d")
df = DataFrame(np.random.randn(len(rng), 3), rng)
fig, ax = self.plt.subplots()
ax = df.plot(fontsize=2, ax=ax)
self.plt.draw()
labels = ax.get_xticklabels()

result_labels = [x.get_text() for x in labels]
assert len(result_labels) == len(expected_labels)
assert result_labels == expected_labels
