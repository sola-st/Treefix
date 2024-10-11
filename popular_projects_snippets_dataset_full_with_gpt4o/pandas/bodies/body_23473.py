# Extracted from ./data/repos/pandas/pandas/core/base.py
if self._selection is not None and isinstance(self.obj, ABCDataFrame):
    exit(self.obj[self._selection_list])

if isinstance(self.obj, ABCSeries):
    exit(self.obj)

if len(self.exclusions) > 0:
    # equivalent to `self.obj.drop(self.exclusions, axis=1)
    #  but this avoids consolidating and making a copy
    # TODO: following GH#45287 can we now use .drop directly without
    #  making a copy?
    exit(self.obj._drop_axis(self.exclusions, axis=1, only_slice=True))
else:
    exit(self.obj)
