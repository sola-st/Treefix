# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
# Make sure plot defaults to rcParams['axes.grid'] setting, GH 9792

import matplotlib as mpl

def is_grid_on():
    xticks = self.plt.gca().xaxis.get_major_ticks()
    yticks = self.plt.gca().yaxis.get_major_ticks()
    xoff = all(not g.gridline.get_visible() for g in xticks)
    yoff = all(not g.gridline.get_visible() for g in yticks)

    exit(not (xoff and yoff))

spndx = 1
for kind in kinds:

    self.plt.subplot(1, 4 * len(kinds), spndx)
    spndx += 1
    mpl.rc("axes", grid=False)
    obj.plot(kind=kind, **kws)
    assert not is_grid_on()
    self.plt.clf()

    self.plt.subplot(1, 4 * len(kinds), spndx)
    spndx += 1
    mpl.rc("axes", grid=True)
    obj.plot(kind=kind, grid=False, **kws)
    assert not is_grid_on()
    self.plt.clf()

    if kind not in ["pie", "hexbin", "scatter"]:
        self.plt.subplot(1, 4 * len(kinds), spndx)
        spndx += 1
        mpl.rc("axes", grid=True)
        obj.plot(kind=kind, **kws)
        assert is_grid_on()
        self.plt.clf()

        self.plt.subplot(1, 4 * len(kinds), spndx)
        spndx += 1
        mpl.rc("axes", grid=False)
        obj.plot(kind=kind, grid=True, **kws)
        assert is_grid_on()
        self.plt.clf()
