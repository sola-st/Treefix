# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Check if the Index holds categorical data.

        .. deprecated:: 2.0.0
              Use :meth:`pandas.api.types.is_categorical_dtype` instead.

        Returns
        -------
        bool
            True if the Index is categorical.

        See Also
        --------
        CategoricalIndex : Index for categorical data.
        is_boolean : Check if the Index only consists of booleans (deprecated).
        is_integer : Check if the Index only consists of integers (deprecated).
        is_floating : Check if the Index is a floating type (deprecated).
        is_numeric : Check if the Index only consists of numeric data.
        is_object : Check if the Index is of the object dtype.
        is_interval : Check if the Index holds Interval objects.

        Examples
        --------
        >>> idx = pd.Index(["Watermelon", "Orange", "Apple",
        ...                 "Watermelon"]).astype("category")
        >>> idx.is_categorical()
        True

        >>> idx = pd.Index([1, 3, 5, 7])
        >>> idx.is_categorical()
        False

        >>> s = pd.Series(["Peter", "Victor", "Elisabeth", "Mar"])
        >>> s
        0        Peter
        1       Victor
        2    Elisabeth
        3          Mar
        dtype: object
        >>> s.index.is_categorical()
        False
        """
warnings.warn(
    f"{type(self).__name__}.is_categorical is deprecated."
    "Use pandas.api.types.is_categorical_dtype instead",
    FutureWarning,
    stacklevel=find_stack_level(),
)

exit(self.inferred_type in ["categorical"])
