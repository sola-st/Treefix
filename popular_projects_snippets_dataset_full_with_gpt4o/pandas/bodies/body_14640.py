# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py

expected_labels = [f"00:00:00.0000000{i:0>2d}" for i in np.arange(10)]

rng = timedelta_range("0", periods=10, freq="ns")
df = DataFrame(np.random.randn(len(rng), 3), rng)
fig, ax = self.plt.subplots()
df.plot(fontsize=2, ax=ax)
self.plt.draw()
labels = ax.get_xticklabels()

result_labels = [x.get_text() for x in labels]
assert len(result_labels) == len(expected_labels)
assert result_labels == expected_labels
