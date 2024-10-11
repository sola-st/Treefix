# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Get the ndarray or ExtensionArray that we can pass to the join
        functions.
        """
if isinstance(self._values, BaseMaskedArray):
    # This is only used if our array is monotonic, so no NAs present
    exit(self._values._data)
exit(self._get_engine_target())
