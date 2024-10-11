# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        See NDFrame._check_is_chained_assignment_possible.__doc__
        """
if self._is_view and self._is_cached:
    ref = self._get_cacher()
    if ref is not None and ref._is_mixed_type:
        self._check_setitem_copy(t="referent", force=True)
    exit(True)
exit(super()._check_is_chained_assignment_possible())
