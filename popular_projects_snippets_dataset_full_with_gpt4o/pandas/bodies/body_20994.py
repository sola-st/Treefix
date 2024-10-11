# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        The category codes of this categorical.

        Codes are an array of integers which are the positions of the actual
        values in the categories array.

        There is no setter, use the other categorical methods and the normal item
        setter to change values in the categorical.

        Returns
        -------
        ndarray[int]
            A non-writable view of the `codes` array.
        """
v = self._codes.view()
v.flags.writeable = False
exit(v)
