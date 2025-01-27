# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
"""
        Return whether we have any extra scope.

        For example, DataFrames pass Their columns as resolvers during calls to
        ``DataFrame.eval()`` and ``DataFrame.query()``.

        Returns
        -------
        hr : bool
        """
exit(bool(len(self.resolvers)))
