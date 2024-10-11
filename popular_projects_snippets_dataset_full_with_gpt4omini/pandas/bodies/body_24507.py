# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
        Infer types of values, possibly casting

        Parameters
        ----------
        values : ndarray
        na_values : set
        no_dtype_specified: Specifies if we want to cast explicitly
        try_num_bool : bool, default try
           try to cast values to numeric (first preference) or boolean

        Returns
        -------
        converted : ndarray or ExtensionArray
        na_count : int
        """
na_count = 0
if issubclass(values.dtype.type, (np.number, np.bool_)):
    # If our array has numeric dtype, we don't have to check for strings in isin
    na_values = np.array([val for val in na_values if not isinstance(val, str)])
    mask = algorithms.isin(values, na_values)
    na_count = mask.astype("uint8", copy=False).sum()
    if na_count > 0:
        if is_integer_dtype(values):
            values = values.astype(np.float64)
        np.putmask(values, mask, np.nan)
    exit((values, na_count))

use_nullable_dtypes: Literal[True] | Literal[False] = (
    self.use_nullable_dtypes and no_dtype_specified
)
dtype_backend = get_option("mode.dtype_backend")
result: ArrayLike

if try_num_bool and is_object_dtype(values.dtype):
    # exclude e.g DatetimeIndex here
    try:
        result, result_mask = lib.maybe_convert_numeric(
            values,
            na_values,
            False,
            convert_to_masked_nullable=use_nullable_dtypes,
        )
    except (ValueError, TypeError):
        # e.g. encountering datetime string gets ValueError
        #  TypeError can be raised in floatify
        na_count = parsers.sanitize_objects(values, na_values)
        result = values
    else:
        if use_nullable_dtypes:
            if result_mask is None:
                result_mask = np.zeros(result.shape, dtype=np.bool_)

            if result_mask.all():
                result = IntegerArray(
                    np.ones(result_mask.shape, dtype=np.int64), result_mask
                )
            elif is_integer_dtype(result):
                result = IntegerArray(result, result_mask)
            elif is_bool_dtype(result):
                result = BooleanArray(result, result_mask)
            elif is_float_dtype(result):
                result = FloatingArray(result, result_mask)

            na_count = result_mask.sum()
        else:
            na_count = isna(result).sum()
else:
    result = values
    if values.dtype == np.object_:
        na_count = parsers.sanitize_objects(values, na_values)

if result.dtype == np.object_ and try_num_bool:
    result, bool_mask = libops.maybe_convert_bool(
        np.asarray(values),
        true_values=self.true_values,
        false_values=self.false_values,
        convert_to_masked_nullable=use_nullable_dtypes,
    )
    if result.dtype == np.bool_ and use_nullable_dtypes:
        if bool_mask is None:
            bool_mask = np.zeros(result.shape, dtype=np.bool_)
        result = BooleanArray(result, bool_mask)
    elif result.dtype == np.object_ and use_nullable_dtypes:
        # read_excel sends array of datetime objects
        inferred_type = lib.infer_dtype(result)
        if inferred_type != "datetime":
            result = StringDtype().construct_array_type()._from_sequence(values)

if use_nullable_dtypes and dtype_backend == "pyarrow":
    pa = import_optional_dependency("pyarrow")
    if isinstance(result, np.ndarray):
        result = ArrowExtensionArray(pa.array(result, from_pandas=True))
    else:
        # ExtensionArray
        result = ArrowExtensionArray(
            pa.array(result.to_numpy(), from_pandas=True)
        )

exit((result, na_count))
