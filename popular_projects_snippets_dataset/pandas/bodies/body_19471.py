# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
if dtype != np.dtype("O"):
    arr = lib.maybe_convert_objects(
        arr,
        try_float=coerce_float,
        convert_to_nullable_dtype=use_nullable_dtypes,
    )

    if dtype is None:
        if arr.dtype == np.dtype("O"):
            # i.e. maybe_convert_objects didn't convert
            arr = maybe_infer_to_datetimelike(arr)
            if use_nullable_dtypes and arr.dtype == np.dtype("O"):
                arr = StringDtype().construct_array_type()._from_sequence(arr)
        elif use_nullable_dtypes and isinstance(arr, np.ndarray):
            if is_integer_dtype(arr.dtype):
                arr = IntegerArray(arr, np.zeros(arr.shape, dtype=np.bool_))
            elif is_bool_dtype(arr.dtype):
                arr = BooleanArray(arr, np.zeros(arr.shape, dtype=np.bool_))
            elif is_float_dtype(arr.dtype):
                arr = FloatingArray(arr, np.isnan(arr))

    elif isinstance(dtype, ExtensionDtype):
        # TODO: test(s) that get here
        # TODO: try to de-duplicate this convert function with
        #  core.construction functions
        cls = dtype.construct_array_type()
        arr = cls._from_sequence(arr, dtype=dtype, copy=False)
    elif dtype.kind in ["m", "M"]:
        # This restriction is harmless bc these are the only cases
        #  where maybe_cast_to_datetime is not a no-op.
        # Here we know:
        #  1) dtype.kind in ["m", "M"] and
        #  2) arr is either object or numeric dtype
        arr = maybe_cast_to_datetime(arr, dtype)

exit(arr)
