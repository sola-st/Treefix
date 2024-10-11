# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py

df = DataFrame(
    np.random.randint(low=0, high=100, size=(6, 4)),
    index=list(string.ascii_letters[:6]),
    columns=["x", "y", "z", "four"],
)

axes = [df.plot.scatter(x="x", y="y", c="z"), df.plot.scatter(x=0, y=1, c=2)]
for ax in axes:
    # default to Greys
    assert ax.collections[0].cmap.name == "Greys"

    assert ax.collections[0].colorbar.ax.get_ylabel() == "z"

cm = "cubehelix"
ax = df.plot.scatter(x="x", y="y", c="z", colormap=cm)
assert ax.collections[0].cmap.name == cm

# verify turning off colorbar works
ax = df.plot.scatter(x="x", y="y", c="z", colorbar=False)
assert ax.collections[0].colorbar is None

# verify that we can still plot a solid color
ax = df.plot.scatter(x=0, y=1, c="red")
assert ax.collections[0].colorbar is None
self._check_colors(ax.collections, facecolors=["r"])

# Ensure that we can pass an np.array straight through to matplotlib,
# this functionality was accidentally removed previously.
# See https://github.com/pandas-dev/pandas/issues/8852 for bug report
#
# Exercise colormap path and non-colormap path as they are independent
#
df = DataFrame({"A": [1, 2], "B": [3, 4]})
red_rgba = [1.0, 0.0, 0.0, 1.0]
green_rgba = [0.0, 1.0, 0.0, 1.0]
rgba_array = np.array([red_rgba, green_rgba])
ax = df.plot.scatter(x="A", y="B", c=rgba_array)
# expect the face colors of the points in the non-colormap path to be
# identical to the values we supplied, normally we'd be on shaky ground
# comparing floats for equality but here we expect them to be
# identical.
tm.assert_numpy_array_equal(ax.collections[0].get_facecolor(), rgba_array)
# we don't test the colors of the faces in this next plot because they
# are dependent on the spring colormap, which may change its colors
# later.
float_array = np.array([0.0, 1.0])
df.plot.scatter(x="A", y="B", c=float_array, cmap="spring")
