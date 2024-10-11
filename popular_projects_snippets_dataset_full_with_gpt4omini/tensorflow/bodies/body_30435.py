# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
super().setUp()
# Create mapping between TensorFlow quantized types and numpy types.
self._quint8 = np.dtype([("quint8", np.uint8)])
self._qint8 = np.dtype([("qint8", np.int8)])
self._qint32 = np.dtype([("qint32", np.int32)])
