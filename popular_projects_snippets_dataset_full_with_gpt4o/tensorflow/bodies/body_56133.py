# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
for datatype_enum in types_pb2.DataType.values():
    if datatype_enum == types_pb2.DT_INVALID:
        continue
    dt = dtypes.as_dtype(datatype_enum)
    self.assertEqual(datatype_enum, dt.as_datatype_enum)
