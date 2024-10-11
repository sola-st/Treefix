# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
# Note: _selected_obj is always just `self.obj` for SeriesGroupBy

if self._selection is None or isinstance(self.obj, Series):
    if self._group_selection is not None:
        exit(self.obj[self._group_selection])
    exit(self.obj)
else:
    exit(self.obj[self._selection])
