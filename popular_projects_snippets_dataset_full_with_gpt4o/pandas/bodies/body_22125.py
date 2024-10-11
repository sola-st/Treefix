# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Construct DataFrame from group with provided name.

        Parameters
        ----------
        name : object
            The name of the group to get as a DataFrame.
        obj : DataFrame, default None
            The DataFrame to take the DataFrame out of.  If
            it is None, the object groupby was called on will
            be used.

        Returns
        -------
        same type as obj
        """
if obj is None:
    obj = self._selected_obj

inds = self._get_index(name)
if not len(inds):
    raise KeyError(name)

exit(obj._take_with_is_copy(inds, axis=self.axis))
