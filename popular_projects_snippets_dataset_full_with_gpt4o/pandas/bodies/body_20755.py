# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Check if the Index is a floating type.

        .. deprecated:: 2.0.0
            Use `pandas.api.types.is_float_dtype` instead

        The Index may consist of only floats, NaNs, or a mix of floats,
        integers, or NaNs.

        Returns
        -------
        bool
            Whether or not the Index only consists of only consists of floats, NaNs, or
            a mix of floats, integers, or NaNs.

        See Also
        --------
        is_boolean : Check if the Index only consists of booleans (deprecated).
        is_integer : Check if the Index only consists of integers (deprecated).
        is_numeric : Check if the Index only consists of numeric data.
        is_object : Check if the Index is of the object dtype.
        is_categorical : Check if the Index holds categorical data (deprecated).
        is_interval : Check if the Index holds Interval objects.

        Examples
        --------
        >>> idx = pd.Index([1.0, 2.0, 3.0, 4.0])
        >>> idx.is_floating()
        True

        >>> idx = pd.Index([1.0, 2.0, np.nan, 4.0])
        >>> idx.is_floating()
        True

        >>> idx = pd.Index([1, 2, 3, 4, np.nan])
        >>> idx.is_floating()
        True

        >>> idx = pd.Index([1, 2, 3, 4])
        >>> idx.is_floating()
        False
        """
warnings.warn(
    f"{type(self).__name__}.is_floating is deprecated. "
    "Use pandas.api.types.is_float_dtype instead.",
    FutureWarning,
    stacklevel=find_stack_level(),
)
exit(self.inferred_type in ["floating", "mixed-integer-float", "integer-na"])
