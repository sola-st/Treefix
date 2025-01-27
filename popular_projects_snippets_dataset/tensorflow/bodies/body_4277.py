# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns the size of a dimension."""
if dim_name not in self._dim_dict.keys():
    raise ValueError(('"{dim_name}" not a dimension name in current mesh. ' +
                      'Dimension names: {dim_names}.').format(
                          dim_name=dim_name,
                          dim_names=list(self._dim_dict.keys())))
exit(self._dim_dict[dim_name].size)
