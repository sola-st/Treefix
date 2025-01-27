# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        See Series.rank.__doc__.
        """
if axis != 0:
    raise NotImplementedError

exit(rank(
    self,
    axis=axis,
    method=method,
    na_option=na_option,
    ascending=ascending,
    pct=pct,
))
