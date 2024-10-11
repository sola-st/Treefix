# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
def _check_colors(bp, box_c, whiskers_c, medians_c, caps_c="k", fliers_c=None):
    # TODO: outside this func?
    if fliers_c is None:
        fliers_c = "k"
    self._check_colors(bp["boxes"], linecolors=[box_c] * len(bp["boxes"]))
    self._check_colors(
        bp["whiskers"], linecolors=[whiskers_c] * len(bp["whiskers"])
    )
    self._check_colors(
        bp["medians"], linecolors=[medians_c] * len(bp["medians"])
    )
    self._check_colors(bp["fliers"], linecolors=[fliers_c] * len(bp["fliers"]))
    self._check_colors(bp["caps"], linecolors=[caps_c] * len(bp["caps"]))

default_colors = self._unpack_cycler(self.plt.rcParams)

df = DataFrame(np.random.randn(5, 5))
bp = df.plot.box(return_type="dict")
_check_colors(
    bp,
    default_colors[0],
    default_colors[0],
    default_colors[2],
    default_colors[0],
)
tm.close()

dict_colors = {
    "boxes": "#572923",
    "whiskers": "#982042",
    "medians": "#804823",
    "caps": "#123456",
}
bp = df.plot.box(color=dict_colors, sym="r+", return_type="dict")
_check_colors(
    bp,
    dict_colors["boxes"],
    dict_colors["whiskers"],
    dict_colors["medians"],
    dict_colors["caps"],
    "r",
)
tm.close()

# partial colors
dict_colors = {"whiskers": "c", "medians": "m"}
bp = df.plot.box(color=dict_colors, return_type="dict")
_check_colors(bp, default_colors[0], "c", "m", default_colors[0])
tm.close()

from matplotlib import cm

# Test str -> colormap functionality
bp = df.plot.box(colormap="jet", return_type="dict")
jet_colors = [cm.jet(n) for n in np.linspace(0, 1, 3)]
_check_colors(bp, jet_colors[0], jet_colors[0], jet_colors[2], jet_colors[0])
tm.close()

# Test colormap functionality
bp = df.plot.box(colormap=cm.jet, return_type="dict")
_check_colors(bp, jet_colors[0], jet_colors[0], jet_colors[2], jet_colors[0])
tm.close()

# string color is applied to all artists except fliers
bp = df.plot.box(color="DodgerBlue", return_type="dict")
_check_colors(bp, "DodgerBlue", "DodgerBlue", "DodgerBlue", "DodgerBlue")

# tuple is also applied to all artists except fliers
bp = df.plot.box(color=(0, 1, 0), sym="#123456", return_type="dict")
_check_colors(bp, (0, 1, 0), (0, 1, 0), (0, 1, 0), (0, 1, 0), "#123456")

msg = re.escape(
    "color dict contains invalid key 'xxxx'. The key must be either "
    "['boxes', 'whiskers', 'medians', 'caps']"
)
with pytest.raises(ValueError, match=msg):
    # Color contains invalid key results in ValueError
    df.plot.box(color={"boxes": "red", "xxxx": "blue"})
