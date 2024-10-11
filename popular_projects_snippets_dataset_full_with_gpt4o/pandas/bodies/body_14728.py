# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_legend.py
# 14563
df = DataFrame(
    {
        "A": [1, 2, 3, 4, 5, 6],
        "B": [2, 4, 1, 3, 2, 4],
        "C": [3, 3, 2, 6, 4, 2],
        "X": [1, 2, 3, 4, 5, 6],
    }
)

fig, ax = self.plt.subplots()
for kind in "ABC":
    df.plot("X", kind, label=kind, ax=ax, style=".")

self._check_legend_labels(ax, labels=["A", "B", "C"])
self._check_legend_marker(ax, expected_markers=[".", ".", "."])
