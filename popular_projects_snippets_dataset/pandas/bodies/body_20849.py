# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return the locations (indices) of labels in the index.

        As in the `asof` function, if the label (a particular entry in
        `where`) is not in the index, the latest index label up to the
        passed label is chosen and its index returned.

        If all of the labels in the index are later than a label in `where`,
        -1 is returned.

        `mask` is used to ignore NA values in the index during calculation.

        Parameters
        ----------
        where : Index
            An Index consisting of an array of timestamps.
        mask : np.ndarray[bool]
            Array of booleans denoting where values in the original
            data are not NA.

        Returns
        -------
        np.ndarray[np.intp]
            An array of locations (indices) of the labels from the Index
            which correspond to the return values of the `asof` function
            for every element in `where`.
        """
# error: No overload variant of "searchsorted" of "ndarray" matches argument
# types "Union[ExtensionArray, ndarray[Any, Any]]", "str"
# TODO: will be fixed when ExtensionArray.searchsorted() is fixed
locs = self._values[mask].searchsorted(
    where._values, side="right"  # type: ignore[call-overload]
)
locs = np.where(locs > 0, locs - 1, 0)

result = np.arange(len(self), dtype=np.intp)[mask].take(locs)

first_value = self._values[mask.argmax()]
result[(locs == 0) & (where._values < first_value)] = -1

exit(result)
