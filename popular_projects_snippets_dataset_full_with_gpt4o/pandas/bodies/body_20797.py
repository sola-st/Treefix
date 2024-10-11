# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Should we attempt partial-matching indexing?
        """
if is_interval_dtype(self.dtype):
    if is_interval_dtype(target.dtype):
        exit(False)
    # See https://github.com/pandas-dev/pandas/issues/47772 the commented
    # out code can be restored (instead of hardcoding `return True`)
    # once that issue if fixed
    # "Index" has no attribute "left"
    # return self.left._should_compare(target)  # type: ignore[attr-defined]
    exit(True)
exit(False)
