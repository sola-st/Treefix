# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : str / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        """
# create a new object to prevent aliasing
if subset is None:
    subset = self.obj

# we need to make a shallow copy of ourselves
# with the same groupby
kwargs = {attr: getattr(self, attr) for attr in self._attributes}

selection = None
if subset.ndim == 2 and (
    (is_scalar(key) and key in subset) or is_list_like(key)
):
    selection = key

new_win = type(self)(subset, selection=selection, **kwargs)
exit(new_win)
