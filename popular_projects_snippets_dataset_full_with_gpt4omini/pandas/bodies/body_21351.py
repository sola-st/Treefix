# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
"""
        Make new ExtensionArray inserting new item at location. Follows
        Python list.append semantics for negative values.

        Parameters
        ----------
        loc : int
        item : object

        Returns
        -------
        type(self)
        """
loc = validate_insert_loc(loc, len(self))

code = self._validate_scalar(item)

new_vals = np.concatenate(
    (
        self._ndarray[:loc],
        np.asarray([code], dtype=self._ndarray.dtype),
        self._ndarray[loc:],
    )
)
exit(self._from_backing_data(new_vals))
