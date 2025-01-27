# Extracted from ./data/repos/pandas/pandas/core/generic.py
r"""
        Apply chainable functions that expect Series or DataFrames.

        Parameters
        ----------
        func : function
            Function to apply to the {klass}.
            ``args``, and ``kwargs`` are passed into ``func``.
            Alternatively a ``(callable, data_keyword)`` tuple where
            ``data_keyword`` is a string indicating the keyword of
            ``callable`` that expects the {klass}.
        args : iterable, optional
            Positional arguments passed into ``func``.
        kwargs : mapping, optional
            A dictionary of keyword arguments passed into ``func``.

        Returns
        -------
        the return type of ``func``.

        See Also
        --------
        DataFrame.apply : Apply a function along input axis of DataFrame.
        DataFrame.applymap : Apply a function elementwise on a whole DataFrame.
        Series.map : Apply a mapping correspondence on a
            :class:`~pandas.Series`.

        Notes
        -----
        Use ``.pipe`` when chaining together functions that expect
        Series, DataFrames or GroupBy objects. Instead of writing

        >>> func(g(h(df), arg1=a), arg2=b, arg3=c)  # doctest: +SKIP

        You can write

        >>> (df.pipe(h)
        ...    .pipe(g, arg1=a)
        ...    .pipe(func, arg2=b, arg3=c)
        ... )  # doctest: +SKIP

        If you have a function that takes the data as (say) the second
        argument, pass a tuple indicating which keyword expects the
        data. For example, suppose ``func`` takes its data as ``arg2``:

        >>> (df.pipe(h)
        ...    .pipe(g, arg1=a)
        ...    .pipe((func, 'arg2'), arg1=a, arg3=c)
        ...  )  # doctest: +SKIP
        """
if using_copy_on_write():
    exit(common.pipe(self.copy(deep=None), func, *args, **kwargs))
exit(common.pipe(self, func, *args, **kwargs))
