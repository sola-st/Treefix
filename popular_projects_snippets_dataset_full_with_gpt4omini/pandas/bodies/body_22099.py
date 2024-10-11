# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
"""
        Return the elements in the given *positional* indices in each group.

        This means that we are not indexing according to actual values in
        the index attribute of the object. We are indexing according to the
        actual position of the element in the object.

        If a requested index does not exist for some group, this method will raise.
        To get similar behavior that ignores indices that don't exist, see
        :meth:`.DataFrameGroupBy.nth`.

        Parameters
        ----------
        indices : array-like
            An array of ints indicating which positions to take.
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            The axis on which to select elements. ``0`` means that we are
            selecting rows, ``1`` means that we are selecting columns.
        **kwargs
            For compatibility with :meth:`numpy.take`. Has no effect on the
            output.

        Returns
        -------
        DataFrame
            An DataFrame containing the elements taken from each group.

        See Also
        --------
        DataFrame.take : Take elements from a Series along an axis.
        DataFrame.loc : Select a subset of a DataFrame by labels.
        DataFrame.iloc : Select a subset of a DataFrame by positions.
        numpy.take : Take elements from an array along an axis.

        Examples
        --------
        >>> df = DataFrame([('falcon', 'bird', 389.0),
        ...                    ('parrot', 'bird', 24.0),
        ...                    ('lion', 'mammal', 80.5),
        ...                    ('monkey', 'mammal', np.nan),
        ...                    ('rabbit', 'mammal', 15.0)],
        ...                   columns=['name', 'class', 'max_speed'],
        ...                   index=[4, 3, 2, 1, 0])
        >>> df
             name   class  max_speed
        4  falcon    bird      389.0
        3  parrot    bird       24.0
        2    lion  mammal       80.5
        1  monkey  mammal        NaN
        0  rabbit  mammal       15.0
        >>> gb = df.groupby([1, 1, 2, 2, 2])

        Take elements at positions 0 and 1 along the axis 0 (default).

        Note how the indices selected in the result do not correspond to
        our input indices 0 and 1. That's because we are selecting the 0th
        and 1st rows, not rows whose indices equal 0 and 1.

        >>> gb.take([0, 1])
               name   class  max_speed
        1 4  falcon    bird      389.0
          3  parrot    bird       24.0
        2 2    lion  mammal       80.5
          1  monkey  mammal        NaN

        The order of the specified indices influnces the order in the result.
        Here, the order is swapped from the previous example.

        >>> gb.take([0, 1])
               name   class  max_speed
        1 4  falcon    bird      389.0
          3  parrot    bird       24.0
        2 2    lion  mammal       80.5
          1  monkey  mammal        NaN

        Take elements at indices 1 and 2 along the axis 1 (column selection).

        We may take elements using negative integers for positive indices,
        starting from the end of the object, just like with Python lists.

        >>> gb.take([-1, -2])
               name   class  max_speed
        1 3  parrot    bird       24.0
          4  falcon    bird      389.0
        2 0  rabbit  mammal       15.0
          1  monkey  mammal        NaN
        """
result = self._op_via_apply("take", indices=indices, axis=axis, **kwargs)
exit(result)
