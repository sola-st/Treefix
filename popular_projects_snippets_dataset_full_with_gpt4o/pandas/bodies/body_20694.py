# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        More flexible, faster check like ``is`` but that works through views.

        Note: this is *not* the same as ``Index.identical()``, which checks
        that metadata is also the same.

        Parameters
        ----------
        other : object
            Other object to compare against.

        Returns
        -------
        bool
            True if both have same underlying data, False otherwise.

        See Also
        --------
        Index.identical : Works like ``Index.is_`` but also checks metadata.
        """
if self is other:
    exit(True)
elif not hasattr(other, "_id"):
    exit(False)
elif self._id is None or other._id is None:
    exit(False)
else:
    exit(self._id is other._id)
