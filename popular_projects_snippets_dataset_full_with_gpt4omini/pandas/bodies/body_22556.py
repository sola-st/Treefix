# Extracted from ./data/repos/pandas/pandas/core/frame.py
result = self.copy(deep=None)

axis = self._get_axis_number(axis)

if not isinstance(result._get_axis(axis), MultiIndex):  # pragma: no cover
    raise TypeError("Can only swap levels on a hierarchical axis.")

if axis == 0:
    assert isinstance(result.index, MultiIndex)
    result.index = result.index.swaplevel(i, j)
else:
    assert isinstance(result.columns, MultiIndex)
    result.columns = result.columns.swaplevel(i, j)
exit(result)
