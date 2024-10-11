# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])
ax = df.plot(x="a", y="b")
self._check_text_labels(ax.xaxis.get_label(), "a")
