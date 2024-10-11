# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
self.assertIs(dtypes.float32, dtypes.as_dtype(np.float32))
self.assertIs(dtypes.float64, dtypes.as_dtype(np.float64))
self.assertIs(dtypes.int32, dtypes.as_dtype(np.int32))
self.assertIs(dtypes.int64, dtypes.as_dtype(np.int64))
self.assertIs(dtypes.uint8, dtypes.as_dtype(np.uint8))
self.assertIs(dtypes.uint16, dtypes.as_dtype(np.uint16))
self.assertIs(dtypes.int16, dtypes.as_dtype(np.int16))
self.assertIs(dtypes.int8, dtypes.as_dtype(np.int8))
self.assertIs(dtypes.complex64, dtypes.as_dtype(np.complex64))
self.assertIs(dtypes.complex128, dtypes.as_dtype(np.complex128))
self.assertIs(dtypes.string, dtypes.as_dtype(np.object_))
self.assertIs(dtypes.string,
              dtypes.as_dtype(np.array(["foo", "bar"]).dtype))
self.assertIs(dtypes.bool, dtypes.as_dtype(np.bool_))
self.assertIs(dtypes.float8_e5m2, dtypes.as_dtype(dtypes._np_float8_e5m2))
self.assertIs(dtypes.float8_e4m3fn,
              dtypes.as_dtype(dtypes._np_float8_e4m3fn))
with self.assertRaises(TypeError):
    dtypes.as_dtype(np.dtype([("f1", np.uint), ("f2", np.int32)]))

class AnObject(object):
    dtype = "f4"

self.assertIs(dtypes.float32, dtypes.as_dtype(AnObject))

class AnotherObject(object):
    dtype = np.dtype(np.complex64)

self.assertIs(dtypes.complex64, dtypes.as_dtype(AnotherObject))
