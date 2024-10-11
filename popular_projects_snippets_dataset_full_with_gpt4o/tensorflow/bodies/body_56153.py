# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
dt = dtypes.DType(types_pb2.DT_VARIANT)
self.assertIs(dtypes.as_dtype(dt), dtypes.variant)
