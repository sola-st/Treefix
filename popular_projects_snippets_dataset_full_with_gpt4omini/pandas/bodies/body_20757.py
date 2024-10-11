# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Check if the Index is of the object dtype.

        Returns
        -------
        bool
            Whether or not the Index is of the object dtype.

        See Also
        --------
        is_boolean : Check if the Index only consists of booleans (deprecated).
        is_integer : Check if the Index only consists of integers (deprecated).
        is_floating : Check if the Index is a floating type (deprecated).
        is_numeric : Check if the Index only consists of numeric data.
        is_categorical : Check if the Index holds categorical data (deprecated).
        is_interval : Check if the Index holds Interval objects.

        Examples
        --------
        >>> idx = pd.Index(["Apple", "Mango", "Watermelon"])
        >>> idx.is_object()
        True

        >>> idx = pd.Index(["Apple", "Mango", 2.0])
        >>> idx.is_object()
        True

        >>> idx = pd.Index(["Watermelon", "Orange", "Apple",
        ...                 "Watermelon"]).astype("category")
        >>> idx.is_object()
        False

        >>> idx = pd.Index([1.0, 2.0, 3.0, 4.0])
        >>> idx.is_object()
        False
        """
exit(is_object_dtype(self.dtype))
