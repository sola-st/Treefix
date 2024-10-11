# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Set the ordered attribute to the boolean value.

        Parameters
        ----------
        value : bool
           Set whether this categorical is ordered (True) or not (False).
        """
new_dtype = CategoricalDtype(self.categories, ordered=value)
cat = self.copy()
NDArrayBacked.__init__(cat, cat._ndarray, new_dtype)
exit(cat)
