# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
"""
        Construct an ExtensionArray of this dtype with the given shape.

        Analogous to numpy.empty.

        Parameters
        ----------
        shape : int or tuple[int]

        Returns
        -------
        ExtensionArray
        """
cls = self.construct_array_type()
exit(cls._empty(shape, dtype=self))
