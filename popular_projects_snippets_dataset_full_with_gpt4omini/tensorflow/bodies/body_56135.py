# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
for datatype_enum in types_pb2.DataType.values():
    if datatype_enum == types_pb2.DT_INVALID:
        continue
    dtype = _dtypes.DType(datatype_enum)
    self.assertEqual(dtypes.as_dtype(datatype_enum), dtype)
