# Extracted from ./data/repos/pandas/pandas/util/_doctools.py
"""
        Plot left / right DataFrames in specified layout.

        Parameters
        ----------
        left : list of DataFrames before operation is applied
        right : DataFrame of operation result
        labels : list of str to be drawn as titles of left DataFrames
        vertical : bool, default True
            If True, use vertical layout. If False, use horizontal layout.
        """
from matplotlib import gridspec
import matplotlib.pyplot as plt

if not isinstance(left, list):
    left = [left]
left = [self._conv(df) for df in left]
right = self._conv(right)

hcells, vcells = self._get_cells(left, right, vertical)

if vertical:
    figsize = self.cell_width * hcells, self.cell_height * vcells
else:
    # include margin for titles
    figsize = self.cell_width * hcells, self.cell_height * vcells
fig = plt.figure(figsize=figsize)

if vertical:
    gs = gridspec.GridSpec(len(left), hcells)
    # left
    max_left_cols = max(self._shape(df)[1] for df in left)
    max_left_rows = max(self._shape(df)[0] for df in left)
    for i, (_left, _label) in enumerate(zip(left, labels)):
        ax = fig.add_subplot(gs[i, 0:max_left_cols])
        self._make_table(ax, _left, title=_label, height=1.0 / max_left_rows)
    # right
    ax = plt.subplot(gs[:, max_left_cols:])
    self._make_table(ax, right, title="Result", height=1.05 / vcells)
    fig.subplots_adjust(top=0.9, bottom=0.05, left=0.05, right=0.95)
else:
    max_rows = max(self._shape(df)[0] for df in left + [right])
    height = 1.0 / np.max(max_rows)
    gs = gridspec.GridSpec(1, hcells)
    # left
    i = 0
    for df, _label in zip(left, labels):
        sp = self._shape(df)
        ax = fig.add_subplot(gs[0, i : i + sp[1]])
        self._make_table(ax, df, title=_label, height=height)
        i += sp[1]
    # right
    ax = plt.subplot(gs[0, i:])
    self._make_table(ax, right, title="Result", height=height)
    fig.subplots_adjust(top=0.85, bottom=0.05, left=0.05, right=0.95)

exit(fig)
