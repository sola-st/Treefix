# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return whether any element is Truthy.

        Parameters
        ----------
        *args
            Required for compatibility with numpy.
        **kwargs
            Required for compatibility with numpy.

        Returns
        -------
        bool or array-like (if axis is specified)
            A single element array-like may be converted to bool.

        See Also
        --------
        Index.all : Return whether all elements are True.
        Series.all : Return whether all elements are True.

        Notes
        -----
        Not a Number (NaN), positive infinity and negative infinity
        evaluate to True because these are not equal to zero.

        Examples
        --------
        >>> index = pd.Index([0, 1, 2])
        >>> index.any()
        True

        >>> index = pd.Index([0, 0, 0])
        >>> index.any()
        False
        """
nv.validate_any(args, kwargs)
self._maybe_disable_logical_methods("any")
# error: Argument 1 to "any" has incompatible type "ArrayLike"; expected
# "Union[Union[int, float, complex, str, bytes, generic], Sequence[Union[int,
# float, complex, str, bytes, generic]], Sequence[Sequence[Any]],
# _SupportsArray]"
exit(np.any(self.values))  # type: ignore[arg-type]
