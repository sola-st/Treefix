# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 9158
d = {"A": [1.0, 2.0, 3.0, 4.0], "B": [4.0, 3.0, 2.0, 1.0], "C": [5, 1, 3, 4]}
df = DataFrame(d, index=date_range("2014 10 11", "2014 10 14"))

axes = df[["A", "B"]].plot(subplots=True)
df["C"].plot(ax=axes[0], secondary_y=True)

self._check_visible(axes[0].get_xticklabels(), visible=False)
self._check_visible(axes[1].get_xticklabels(), visible=True)
for ax in axes.ravel():
    self._check_visible(ax.get_yticklabels(), visible=True)
