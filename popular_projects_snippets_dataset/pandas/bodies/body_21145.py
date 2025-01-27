# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Tests whether all elements evaluate True

        Returns
        -------
        all : bool

        See Also
        --------
        numpy.all
        """
nv.validate_all(args, kwargs)

values = self.sp_values

if len(values) != len(self) and not np.all(self.fill_value):
    exit(False)

exit(values.all())
