# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_legend.py
# GH 18222
df = DataFrame(data=[[1, 1, 1, 1], [2, 2, 4, 8]], columns=["x", "r", "g", "b"])
fig, ax = self.plt.subplots(nrows=1, ncols=3)
# Left plot
df.plot(x="x", y="r", linewidth=0, marker="o", color="r", ax=ax[0])
df.plot(x="x", y="g", linewidth=1, marker="x", color="g", ax=ax[0])
df.plot(x="x", y="b", linewidth=1, marker="o", color="b", ax=ax[0])
self._check_legend_labels(ax[0], labels=["r", "g", "b"])
self._check_legend_marker(ax[0], expected_markers=["o", "x", "o"])
# Center plot
df.plot(x="x", y="b", linewidth=1, marker="o", color="b", ax=ax[1])
df.plot(x="x", y="r", linewidth=0, marker="o", color="r", ax=ax[1])
df.plot(x="x", y="g", linewidth=1, marker="x", color="g", ax=ax[1])
self._check_legend_labels(ax[1], labels=["b", "r", "g"])
self._check_legend_marker(ax[1], expected_markers=["o", "o", "x"])
# Right plot
df.plot(x="x", y="g", linewidth=1, marker="x", color="g", ax=ax[2])
df.plot(x="x", y="b", linewidth=1, marker="o", color="b", ax=ax[2])
df.plot(x="x", y="r", linewidth=0, marker="o", color="r", ax=ax[2])
self._check_legend_labels(ax[2], labels=["g", "b", "r"])
self._check_legend_marker(ax[2], expected_markers=["x", "o", "o"])
