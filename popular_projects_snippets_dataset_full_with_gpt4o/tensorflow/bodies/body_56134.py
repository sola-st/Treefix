# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
for datatype_enum in types_pb2.DataType.values():
    if not _is_numeric_dtype_enum(datatype_enum):
        continue
    dtype = dtypes.as_dtype(datatype_enum)
    numpy_dtype = dtype.as_numpy_dtype
    _ = np.empty((1, 1, 1, 1), dtype=numpy_dtype)
    if dtype.base_dtype != dtypes.bfloat16:
        # NOTE(touts): Intentionally no way to feed a DT_BFLOAT16.
        self.assertEqual(
            dtypes.as_dtype(datatype_enum).base_dtype,
            dtypes.as_dtype(numpy_dtype))
