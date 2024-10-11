# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 6667
df = DataFrame(np.random.rand(10, 3), index=list(string.ascii_letters[:10]))

axes = df.plot(subplots=True, layout=(2, 2))
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))
assert axes.shape == (2, 2)

axes = df.plot(subplots=True, layout=(-1, 2))
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))
assert axes.shape == (2, 2)

axes = df.plot(subplots=True, layout=(2, -1))
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))
assert axes.shape == (2, 2)

axes = df.plot(subplots=True, layout=(1, 4))
self._check_axes_shape(axes, axes_num=3, layout=(1, 4))
assert axes.shape == (1, 4)

axes = df.plot(subplots=True, layout=(-1, 4))
self._check_axes_shape(axes, axes_num=3, layout=(1, 4))
assert axes.shape == (1, 4)

axes = df.plot(subplots=True, layout=(4, -1))
self._check_axes_shape(axes, axes_num=3, layout=(4, 1))
assert axes.shape == (4, 1)

msg = "Layout of 1x1 must be larger than required size 3"

with pytest.raises(ValueError, match=msg):
    df.plot(subplots=True, layout=(1, 1))

msg = "At least one dimension of layout must be positive"
with pytest.raises(ValueError, match=msg):
    df.plot(subplots=True, layout=(-1, -1))
