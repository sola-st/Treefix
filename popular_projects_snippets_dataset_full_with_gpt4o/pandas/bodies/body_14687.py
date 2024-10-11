# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py

# GH 6667
df = DataFrame(np.random.rand(10, 1), index=list(string.ascii_letters[:10]))
axes = df.plot(subplots=True, **kwargs)
self._check_axes_shape(
    axes,
    axes_num=expected_axes_num,
    layout=expected_layout,
)
assert axes.shape == expected_shape
