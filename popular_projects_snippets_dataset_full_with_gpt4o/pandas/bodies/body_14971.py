# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
xticks = self.plt.gca().xaxis.get_major_ticks()
yticks = self.plt.gca().yaxis.get_major_ticks()
xoff = all(not g.gridline.get_visible() for g in xticks)
yoff = all(not g.gridline.get_visible() for g in yticks)

exit(not (xoff and yoff))
