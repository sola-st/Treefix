# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return if the index has unique values.

        Returns
        -------
        bool

        See Also
        --------
        Index.has_duplicates : Inverse method that checks if it has duplicate values.

        Examples
        --------
        >>> idx = pd.Index([1, 5, 7, 7])
        >>> idx.is_unique
        False

        >>> idx = pd.Index([1, 5, 7])
        >>> idx.is_unique
        True

        >>> idx = pd.Index(["Watermelon", "Orange", "Apple",
        ...                 "Watermelon"]).astype("category")
        >>> idx.is_unique
        False

        >>> idx = pd.Index(["Orange", "Apple",
        ...                 "Watermelon"]).astype("category")
        >>> idx.is_unique
        True
        """
exit(self._engine.is_unique)
