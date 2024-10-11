# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# https://github.com/pandas-dev/pandas/issues/9737 using gridspec,
# the axis in fig.get_axis() are sorted differently than pandas
# expected them, so make sure that only the right ones are removed
import matplotlib.pyplot as plt

plt.close("all")
gs, axes = _generate_4_axes_via_gridspec()

df = DataFrame(
    {
        "a": [1, 2, 3, 4, 5, 6],
        "b": [1, 2, 3, 4, 5, 6],
        "c": [1, 2, 3, 4, 5, 6],
        "d": [1, 2, 3, 4, 5, 6],
    }
)

def _check(axes):
    for ax in axes:
        assert len(ax.lines) == 1
        self._check_visible(ax.get_yticklabels(), visible=True)
    for ax in [axes[0], axes[2]]:
        self._check_visible(ax.get_xticklabels(), visible=False)
        self._check_visible(ax.get_xticklabels(minor=True), visible=False)
    for ax in [axes[1], axes[3]]:
        self._check_visible(ax.get_xticklabels(), visible=True)
        self._check_visible(ax.get_xticklabels(minor=True), visible=True)

for ax in axes:
    df.plot(x="a", y="b", title="title", ax=ax, sharex=True)
gs.tight_layout(plt.gcf())
_check(axes)
tm.close()

gs, axes = _generate_4_axes_via_gridspec()
with tm.assert_produces_warning(UserWarning):
    axes = df.plot(subplots=True, ax=axes, sharex=True)
_check(axes)
tm.close()

gs, axes = _generate_4_axes_via_gridspec()
# without sharex, no labels should be touched!
for ax in axes:
    df.plot(x="a", y="b", title="title", ax=ax)

gs.tight_layout(plt.gcf())
for ax in axes:
    assert len(ax.lines) == 1
    self._check_visible(ax.get_yticklabels(), visible=True)
    self._check_visible(ax.get_xticklabels(), visible=True)
    self._check_visible(ax.get_xticklabels(minor=True), visible=True)
tm.close()
