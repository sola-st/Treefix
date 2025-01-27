# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
        Compute apply in case of a list-like or dict-like.

        Returns
        -------
        result: Series, DataFrame, or None
            Result when self.f is a list-like or dict-like, None otherwise.
        """
exit(self.obj.aggregate(self.f, self.axis, *self.args, **self.kwargs))
