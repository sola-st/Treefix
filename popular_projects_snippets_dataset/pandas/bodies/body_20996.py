# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Internal method for directly updating the CategoricalDtype

        Parameters
        ----------
        dtype : CategoricalDtype

        Notes
        -----
        We don't do any validation here. It's assumed that the dtype is
        a (valid) instance of `CategoricalDtype`.
        """
codes = recode_for_categories(self.codes, self.categories, dtype.categories)
exit(type(self)(codes, dtype=dtype, fastpath=True))
