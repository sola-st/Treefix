# Extracted from ./data/repos/pandas/pandas/util/_doctools.py
if df is None:
    ax.set_visible(False)
    exit()

from pandas import plotting

idx_nlevels = df.index.nlevels
col_nlevels = df.columns.nlevels
# must be convert here to get index levels for colorization
df = self._insert_index(df)
tb = plotting.table(ax, df, loc=9)
tb.set_fontsize(self.font_size)

if height is None:
    height = 1.0 / (len(df) + 1)

props = tb.properties()
for (r, c), cell in props["celld"].items():
    if c == -1:
        cell.set_visible(False)
    elif r < col_nlevels and c < idx_nlevels:
        cell.set_visible(False)
    elif r < col_nlevels or c < idx_nlevels:
        cell.set_facecolor("#AAAAAA")
    cell.set_height(height)

ax.set_title(title, size=self.font_size)
ax.axis("off")
