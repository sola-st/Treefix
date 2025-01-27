# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Return the elements in the given *positional* indices along an axis.

        This means that we are not indexing according to actual values in
        the index attribute of the object. We are indexing according to the
        actual position of the element in the object.

        Parameters
        ----------
        indices : array-like
            An array of ints indicating which positions to take.
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            The axis on which to select elements. ``0`` means that we are
            selecting rows, ``1`` means that we are selecting columns.
            For `Series` this parameter is unused and defaults to 0.
        **kwargs
            For compatibility with :meth:`numpy.take`. Has no effect on the
            output.

        Returns
        -------
        same type as caller
            An array-like containing the elements taken from the object.

        See Also
        --------
        DataFrame.loc : Select a subset of a DataFrame by labels.
        DataFrame.iloc : Select a subset of a DataFrame by positions.
        numpy.take : Take elements from an array along an axis.

        Examples
        --------
        >>> df = pd.DataFrame([('falcon', 'bird', 389.0),
        ...                    ('parrot', 'bird', 24.0),
        ...                    ('lion', 'mammal', 80.5),
        ...                    ('monkey', 'mammal', np.nan)],
        ...                   columns=['name', 'class', 'max_speed'],
        ...                   index=[0, 2, 3, 1])
        >>> df
             name   class  max_speed
        0  falcon    bird      389.0
        2  parrot    bird       24.0
        3    lion  mammal       80.5
        1  monkey  mammal        NaN

        Take elements at positions 0 and 3 along the axis 0 (default).

        Note how the actual indices selected (0 and 1) do not correspond to
        our selected indices 0 and 3. That's because we are selecting the 0th
        and 3rd rows, not rows whose indices equal 0 and 3.

        >>> df.take([0, 3])
             name   class  max_speed
        0  falcon    bird      389.0
        1  monkey  mammal        NaN

        Take elements at indices 1 and 2 along the axis 1 (column selection).

        >>> df.take([1, 2], axis=1)
            class  max_speed
        0    bird      389.0
        2    bird       24.0
        3  mammal       80.5
        1  mammal        NaN

        We may take elements using negative integers for positive indices,
        starting from the end of the object, just like with Python lists.

        >>> df.take([-1, -2])
             name   class  max_speed
        1  monkey  mammal        NaN
        3    lion  mammal       80.5
        """

nv.validate_take((), kwargs)

exit(self._take(indices, axis))
