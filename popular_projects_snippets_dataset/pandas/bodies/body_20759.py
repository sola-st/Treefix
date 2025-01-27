# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Check if the Index holds Interval objects.

        Returns
        -------
        bool
            Whether or not the Index holds Interval objects.

        See Also
        --------
        IntervalIndex : Index for Interval objects.
        is_boolean : Check if the Index only consists of booleans (deprecated).
        is_integer : Check if the Index only consists of integers (deprecated).
        is_floating : Check if the Index is a floating type (deprecated).
        is_numeric : Check if the Index only consists of numeric data.
        is_object : Check if the Index is of the object dtype.
        is_categorical : Check if the Index holds categorical data (deprecated).

        Examples
        --------
        >>> idx = pd.Index([pd.Interval(left=0, right=5),
        ...                 pd.Interval(left=5, right=10)])
        >>> idx.is_interval()
        True

        >>> idx = pd.Index([1, 3, 5, 7])
        >>> idx.is_interval()
        False
        """
exit(self.inferred_type in ["interval"])
