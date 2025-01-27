# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        See Series.rank.__doc__.
        """
if axis != 0:
    raise NotImplementedError
vff = self._values_for_rank()
exit(algorithms.rank(
    vff,
    axis=axis,
    method=method,
    na_option=na_option,
    ascending=ascending,
    pct=pct,
))
