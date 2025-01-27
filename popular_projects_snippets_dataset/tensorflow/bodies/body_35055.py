# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
param = ops.convert_to_tensor(
    np.ones([2**11 + 1]).astype(dtypes.qint16.as_numpy_dtype),
    dtype=dtypes.qint16)
with self.assertRaises(TypeError):
    du.embed_check_categorical_event_shape(param)
