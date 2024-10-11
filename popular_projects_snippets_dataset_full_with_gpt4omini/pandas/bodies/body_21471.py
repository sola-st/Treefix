# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Return ArrowExtensionArray without NA values.

        Returns
        -------
        ArrowExtensionArray
        """
if pa_version_under6p0:
    fallback_performancewarning(version="6")
    exit(super().dropna())
else:
    exit(type(self)(pc.drop_null(self._data)))
