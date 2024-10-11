# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Return {klass} with requested index / column level(s) removed.

        Parameters
        ----------
        level : int, str, or list-like
            If a string is given, must be the name of a level
            If list-like, elements must be names or positional indexes
            of levels.

        axis : {{0 or 'index', 1 or 'columns'}}, default 0
            Axis along which the level(s) is removed:

            * 0 or 'index': remove level(s) in column.
            * 1 or 'columns': remove level(s) in row.

            For `Series` this parameter is unused and defaults to 0.

        Returns
        -------
        {klass}
            {klass} with requested index / column level(s) removed.

        Examples
        --------
        >>> df = pd.DataFrame([
        ...     [1, 2, 3, 4],
        ...     [5, 6, 7, 8],
        ...     [9, 10, 11, 12]
        ... ]).set_index([0, 1]).rename_axis(['a', 'b'])

        >>> df.columns = pd.MultiIndex.from_tuples([
        ...     ('c', 'e'), ('d', 'f')
        ... ], names=['level_1', 'level_2'])

        >>> df
        level_1   c   d
        level_2   e   f
        a b
        1 2      3   4
        5 6      7   8
        9 10    11  12

        >>> df.droplevel('a')
        level_1   c   d
        level_2   e   f
        b
        2        3   4
        6        7   8
        10      11  12

        >>> df.droplevel('level_2', axis=1)
        level_1   c   d
        a b
        1 2      3   4
        5 6      7   8
        9 10    11  12
        """
labels = self._get_axis(axis)
new_labels = labels.droplevel(level)
exit(self.set_axis(new_labels, axis=axis, copy=None))
