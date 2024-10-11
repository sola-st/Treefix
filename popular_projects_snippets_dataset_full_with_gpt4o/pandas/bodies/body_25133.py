# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if self.table is False:
    exit()
elif self.table is True:
    data = self.data.transpose()
else:
    data = self.table
ax = self._get_ax(0)
tools.table(ax, data)
