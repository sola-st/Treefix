# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
for datatype_enum in types_pb2.DataType.values():
    if datatype_enum == types_pb2.DT_INVALID:
        continue
    self.assertEqual(datatype_enum,
                     dtypes.DType(datatype_enum).as_datatype_enum)
