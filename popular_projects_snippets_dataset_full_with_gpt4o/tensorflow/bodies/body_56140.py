# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
dtypez = []
names = set()
for datatype_enum in types_pb2.DataType.values():
    if datatype_enum == types_pb2.DT_INVALID:
        continue
    dtype = dtypes.as_dtype(datatype_enum)
    dtypez.append(dtype)
    names.add(dtype.name)
self.assertEqual(len(dtypez), len(names))
