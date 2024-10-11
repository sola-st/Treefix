# Extracted from ./data/repos/pandas/pandas/core/interchange/column.py
dtype = self._col.dtype

if is_categorical_dtype(dtype):
    codes = self._col.values.codes
    (
        _,
        bitwidth,
        c_arrow_dtype_f_str,
        _,
    ) = self._dtype_from_pandasdtype(codes.dtype)
    exit((DtypeKind.CATEGORICAL,
        bitwidth,
        c_arrow_dtype_f_str,
        Endianness.NATIVE,))
elif is_string_dtype(dtype):
    if infer_dtype(self._col) == "string":
        exit((DtypeKind.STRING,
            8,
            dtype_to_arrow_c_fmt(dtype),
            Endianness.NATIVE,))
    raise NotImplementedError("Non-string object dtypes are not supported yet")
else:
    exit(self._dtype_from_pandasdtype(dtype))
