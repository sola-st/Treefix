# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
# make sure min/max evaluates for all data types that have min/max
for datatype_enum in types_pb2.DataType.values():
    if not _is_numeric_dtype_enum(datatype_enum):
        continue
    dtype = dtypes.as_dtype(datatype_enum)
    numpy_dtype = dtype.as_numpy_dtype

    # ignore types for which there are no minimum/maximum (or we cannot
    # compute it, such as for the q* types)
    if (dtype.is_quantized or dtype.base_dtype == dtypes.bool or
        dtype.base_dtype == dtypes.string or
        dtype.base_dtype == dtypes.complex64 or
        dtype.base_dtype == dtypes.complex128):
        continue

    print("%s: %s - %s" % (dtype, dtype.min, dtype.max))

    # check some values that are known
    if numpy_dtype == np.bool_:
        self.assertEqual(dtype.min, 0)
        self.assertEqual(dtype.max, 1)
    if numpy_dtype == np.int8:
        self.assertEqual(dtype.min, -128)
        self.assertEqual(dtype.max, 127)
    if numpy_dtype == np.int16:
        self.assertEqual(dtype.min, -32768)
        self.assertEqual(dtype.max, 32767)
    if numpy_dtype == np.int32:
        self.assertEqual(dtype.min, -2147483648)
        self.assertEqual(dtype.max, 2147483647)
    if numpy_dtype == np.int64:
        self.assertEqual(dtype.min, -9223372036854775808)
        self.assertEqual(dtype.max, 9223372036854775807)
    if numpy_dtype == np.uint8:
        self.assertEqual(dtype.min, 0)
        self.assertEqual(dtype.max, 255)
    if numpy_dtype == np.uint16:
        if dtype == dtypes.uint16:
            self.assertEqual(dtype.min, 0)
            self.assertEqual(dtype.max, 65535)
        elif dtype == dtypes.bfloat16:
            self.assertEqual(dtype.min, 0)
            self.assertEqual(dtype.max, 4294967295)
    if numpy_dtype == np.uint32:
        self.assertEqual(dtype.min, 0)
        self.assertEqual(dtype.max, 4294967295)
    if numpy_dtype == np.uint64:
        self.assertEqual(dtype.min, 0)
        self.assertEqual(dtype.max, 18446744073709551615)
    if numpy_dtype in (np.float16, np.float32, np.float64):
        self.assertEqual(dtype.min, np.finfo(numpy_dtype).min)
        self.assertEqual(dtype.max, np.finfo(numpy_dtype).max)
    if numpy_dtype == dtypes.bfloat16.as_numpy_dtype:
        self.assertEqual(dtype.min, float.fromhex("-0x1.FEp127"))
        self.assertEqual(dtype.max, float.fromhex("0x1.FEp127"))
    if numpy_dtype == dtypes.float8_e5m2.as_numpy_dtype:
        self.assertEqual(dtype.min, -57344.0)
        self.assertEqual(dtype.max, 57344.0)
    if numpy_dtype == dtypes.float8_e4m3fn.as_numpy_dtype:
        self.assertEqual(dtype.min, -448.0)
        self.assertEqual(dtype.max, 448.0)
