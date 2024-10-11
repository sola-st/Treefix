# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
for enum in dtypes._TYPE_TO_STRING:
    dtype = dtypes.DType(enum)
    ctor, args = dtype.__reduce__()
    self.assertEqual(ctor, dtypes.as_dtype)
    self.assertEqual(args, (dtype.name,))
    reconstructed = ctor(*args)
    self.assertEqual(reconstructed, dtype)
