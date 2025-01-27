# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# https://github.com/pandas-dev/pandas/issues/34316

df = DataFrame(
    [[5.1, 3.5], [4.9, 3.0], [7.0, 3.2], [6.4, 3.2], [5.9, 3.0]],
    columns=["length", "width"],
)
df["species"] = ["r", "r", "g", "g", "b"]
if cmap is not None:
    with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
        ax = df.plot.scatter(x=0, y=1, cmap=cmap, c="species")
else:
    ax = df.plot.scatter(x=0, y=1, c="species", cmap=cmap)
assert ax.collections[0].colorbar is None
