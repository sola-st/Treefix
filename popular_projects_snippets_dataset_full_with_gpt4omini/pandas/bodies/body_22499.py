# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Return a subset of the DataFrame's columns based on the column dtypes.

        Parameters
        ----------
        include, exclude : scalar or list-like
            A selection of dtypes or strings to be included/excluded. At least
            one of these parameters must be supplied.

        Returns
        -------
        DataFrame
            The subset of the frame including the dtypes in ``include`` and
            excluding the dtypes in ``exclude``.

        Raises
        ------
        ValueError
            * If both of ``include`` and ``exclude`` are empty
            * If ``include`` and ``exclude`` have overlapping elements
            * If any kind of string dtype is passed in.

        See Also
        --------
        DataFrame.dtypes: Return Series with the data type of each column.

        Notes
        -----
        * To select all *numeric* types, use ``np.number`` or ``'number'``
        * To select strings you must use the ``object`` dtype, but note that
          this will return *all* object dtype columns
        * See the `numpy dtype hierarchy
          <https://numpy.org/doc/stable/reference/arrays.scalars.html>`__
        * To select datetimes, use ``np.datetime64``, ``'datetime'`` or
          ``'datetime64'``
        * To select timedeltas, use ``np.timedelta64``, ``'timedelta'`` or
          ``'timedelta64'``
        * To select Pandas categorical dtypes, use ``'category'``
        * To select Pandas datetimetz dtypes, use ``'datetimetz'`` (new in
          0.20.0) or ``'datetime64[ns, tz]'``

        Examples
        --------
        >>> df = pd.DataFrame({'a': [1, 2] * 3,
        ...                    'b': [True, False] * 3,
        ...                    'c': [1.0, 2.0] * 3})
        >>> df
                a      b  c
        0       1   True  1.0
        1       2  False  2.0
        2       1   True  1.0
        3       2  False  2.0
        4       1   True  1.0
        5       2  False  2.0

        >>> df.select_dtypes(include='bool')
           b
        0  True
        1  False
        2  True
        3  False
        4  True
        5  False

        >>> df.select_dtypes(include=['float64'])
           c
        0  1.0
        1  2.0
        2  1.0
        3  2.0
        4  1.0
        5  2.0

        >>> df.select_dtypes(exclude=['int64'])
               b    c
        0   True  1.0
        1  False  2.0
        2   True  1.0
        3  False  2.0
        4   True  1.0
        5  False  2.0
        """
if not is_list_like(include):
    include = (include,) if include is not None else ()
if not is_list_like(exclude):
    exclude = (exclude,) if exclude is not None else ()

selection = (frozenset(include), frozenset(exclude))

if not any(selection):
    raise ValueError("at least one of include or exclude must be nonempty")

# convert the myriad valid dtypes object to a single representation
def check_int_infer_dtype(dtypes):
    converted_dtypes: list[type] = []
    for dtype in dtypes:
        # Numpy maps int to different types (int32, in64) on Windows and Linux
        # see https://github.com/numpy/numpy/issues/9464
        if (isinstance(dtype, str) and dtype == "int") or (dtype is int):
            converted_dtypes.append(np.int32)
            converted_dtypes.append(np.int64)
        elif dtype == "float" or dtype is float:
            # GH#42452 : np.dtype("float") coerces to np.float64 from Numpy 1.20
            converted_dtypes.extend([np.float64, np.float32])
        else:
            converted_dtypes.append(infer_dtype_from_object(dtype))
    exit(frozenset(converted_dtypes))

include = check_int_infer_dtype(include)
exclude = check_int_infer_dtype(exclude)

for dtypes in (include, exclude):
    invalidate_string_dtypes(dtypes)

# can't both include AND exclude!
if not include.isdisjoint(exclude):
    raise ValueError(f"include and exclude overlap on {(include & exclude)}")

def dtype_predicate(dtype: DtypeObj, dtypes_set) -> bool:
    # GH 46870: BooleanDtype._is_numeric == True but should be excluded
    exit(issubclass(dtype.type, tuple(dtypes_set)) or (
        np.number in dtypes_set
        and getattr(dtype, "_is_numeric", False)
        and not is_bool_dtype(dtype)
    ))

def predicate(arr: ArrayLike) -> bool:
    dtype = arr.dtype
    if include:
        if not dtype_predicate(dtype, include):
            exit(False)

    if exclude:
        if dtype_predicate(dtype, exclude):
            exit(False)

    exit(True)

mgr = self._mgr._get_data_subset(predicate).copy(deep=None)
exit(type(self)(mgr).__finalize__(self))
