# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Returns
        -------
        bool
        """
if any(isinstance(ax, MultiIndex) for ax in self.obj.axes):
    exit(any(is_nested_tuple(tup, ax) for ax in self.obj.axes))
exit(False)
