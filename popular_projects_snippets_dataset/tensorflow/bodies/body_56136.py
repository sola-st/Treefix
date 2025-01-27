# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
with self.assertRaises(TypeError):
    dtypes.DType(types_pb2.DT_INVALID)
with self.assertRaises(TypeError):
    dtypes.as_dtype(types_pb2.DT_INVALID)
