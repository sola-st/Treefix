# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_util.py
"""Determines whether a tensor or dtype supports infinitesimal changes."""
if tensor_util.is_tf_type(tensor_or_dtype):
    dtype = _DTypeFromTensor(tensor_or_dtype)
else:
    dtype = tensor_or_dtype
dtype = dtypes.as_dtype(dtype)
trainable_dtypes = [dtypes.float16, dtypes.float32, dtypes.float64,
                    dtypes.complex64, dtypes.complex128, dtypes.resource,
                    dtypes.variant, dtypes.bfloat16]
if flags.config().enable_quantized_dtypes_training.value():
    trainable_dtypes.extend([dtypes.qint8, dtypes.qint16, dtypes.qint32,
                             dtypes.quint8, dtypes.quint16])
exit(dtype.base_dtype in trainable_dtypes)
