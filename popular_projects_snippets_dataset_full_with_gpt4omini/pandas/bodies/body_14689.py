# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 5353, 6970, GH 7069
fig, axes = self.plt.subplots(2, 3)
df = DataFrame(np.random.rand(10, 3), index=list(string.ascii_letters[:10]))

returned = df.plot(subplots=True, ax=axes[0], sharex=False, sharey=False)
self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
assert returned.shape == (3,)
assert returned[0].figure is fig
# draw on second row
returned = df.plot(subplots=True, ax=axes[1], sharex=False, sharey=False)
self._check_axes_shape(returned, axes_num=3, layout=(1, 3))
assert returned.shape == (3,)
assert returned[0].figure is fig
self._check_axes_shape(axes, axes_num=6, layout=(2, 3))
tm.close()

msg = "The number of passed axes must be 3, the same as the output plot"

with pytest.raises(ValueError, match=msg):
    fig, axes = self.plt.subplots(2, 3)
    # pass different number of axes from required
    df.plot(subplots=True, ax=axes)

# pass 2-dim axes and invalid layout
# invalid lauout should not affect to input and return value
# (show warning is tested in
# TestDataFrameGroupByPlots.test_grouped_box_multiple_axes
fig, axes = self.plt.subplots(2, 2)
with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    df = DataFrame(np.random.rand(10, 4), index=list(string.ascii_letters[:10]))

    returned = df.plot(
        subplots=True, ax=axes, layout=(2, 1), sharex=False, sharey=False
    )
    self._check_axes_shape(returned, axes_num=4, layout=(2, 2))
    assert returned.shape == (4,)

    returned = df.plot(
        subplots=True, ax=axes, layout=(2, -1), sharex=False, sharey=False
    )
    self._check_axes_shape(returned, axes_num=4, layout=(2, 2))
    assert returned.shape == (4,)

    returned = df.plot(
        subplots=True, ax=axes, layout=(-1, 2), sharex=False, sharey=False
    )
self._check_axes_shape(returned, axes_num=4, layout=(2, 2))
assert returned.shape == (4,)

# single column
fig, axes = self.plt.subplots(1, 1)
df = DataFrame(np.random.rand(10, 1), index=list(string.ascii_letters[:10]))

axes = df.plot(subplots=True, ax=[axes], sharex=False, sharey=False)
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
assert axes.shape == (1,)
