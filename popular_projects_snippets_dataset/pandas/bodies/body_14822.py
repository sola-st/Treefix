# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
d = {
    "a": np.arange(10),
    "b": np.arange(10) + 1,
    "c": np.arange(10) + 1,
    "d": np.arange(10),
    "e": np.arange(10),
}
df = DataFrame(d)

axes = df.plot(subplots=[("b", "e"), ("c", "d")], kind=kind)
assert len(axes) == 3  # 2 groups + single column a

expected_labels = (["b", "e"], ["c", "d"], ["a"])
for ax, labels in zip(axes, expected_labels):
    if kind != "pie":
        self._check_legend_labels(ax, labels=labels)
    if kind == "line":
        assert len(ax.lines) == len(labels)
