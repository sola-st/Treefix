# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Internal version of the `take` method that sets the `_is_copy`
        attribute to keep track of the parent dataframe (using in indexing
        for the SettingWithCopyWarning). For Series this does the same
        as the public take (it never sets `_is_copy`).

        See the docstring of `take` for full explanation of the parameters.
        """
exit(self.take(indices=indices, axis=axis))
