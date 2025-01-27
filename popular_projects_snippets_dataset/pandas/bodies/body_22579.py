# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : string / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        """
if subset is None:
    subset = self
elif subset.ndim == 1:  # is Series
    exit(subset)

# TODO: _shallow_copy(subset)?
exit(subset[key])
