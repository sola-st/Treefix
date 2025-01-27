# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
for ax in axes:
    assert len(ax.lines) == 1
    self._check_visible(ax.get_xticklabels(), visible=True)
    self._check_visible(ax.get_xticklabels(minor=True), visible=True)
for ax in [axes[0], axes[1]]:
    self._check_visible(ax.get_yticklabels(), visible=True)
for ax in [axes[2], axes[3]]:
    self._check_visible(ax.get_yticklabels(), visible=False)
