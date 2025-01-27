# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 10657
import matplotlib.pyplot as plt

df = DataFrame(
    np.random.randn(10, 2),
    index=date_range("1/1/2000", periods=10),
    columns=list("AB"),
)

# shared subplots
fig, axes = plt.subplots(2, 1, sharex=True)
axes = df.plot(subplots=True, ax=axes)
for ax in axes:
    assert len(ax.lines) == 1
    self._check_visible(ax.get_yticklabels(), visible=True)
# xaxis of 1st ax must be hidden
self._check_visible(axes[0].get_xticklabels(), visible=False)
self._check_visible(axes[0].get_xticklabels(minor=True), visible=False)
self._check_visible(axes[1].get_xticklabels(), visible=True)
self._check_visible(axes[1].get_xticklabels(minor=True), visible=True)
tm.close()

fig, axes = plt.subplots(2, 1)
with tm.assert_produces_warning(UserWarning):
    axes = df.plot(subplots=True, ax=axes, sharex=True)
for ax in axes:
    assert len(ax.lines) == 1
    self._check_visible(ax.get_yticklabels(), visible=True)
# xaxis of 1st ax must be hidden
self._check_visible(axes[0].get_xticklabels(), visible=False)
self._check_visible(axes[0].get_xticklabels(minor=True), visible=False)
self._check_visible(axes[1].get_xticklabels(), visible=True)
self._check_visible(axes[1].get_xticklabels(minor=True), visible=True)
tm.close()

# not shared
fig, axes = plt.subplots(2, 1)
axes = df.plot(subplots=True, ax=axes)
for ax in axes:
    assert len(ax.lines) == 1
    self._check_visible(ax.get_yticklabels(), visible=True)
    self._check_visible(ax.get_xticklabels(), visible=True)
    self._check_visible(ax.get_xticklabels(minor=True), visible=True)
tm.close()
