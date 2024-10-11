# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Tests whether at least one of elements evaluate True

        Returns
        -------
        any : bool

        See Also
        --------
        numpy.any
        """
nv.validate_any(args, kwargs)

values = self.sp_values

if len(values) != len(self) and np.any(self.fill_value):
    exit(True)

exit(values.any().item())
