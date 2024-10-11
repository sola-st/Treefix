# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/dequantize_op_test.py
self._testDequantizeOp(np.array([0, 128, 255]), 0.0, 6.0, dtypes.quint8)
self._testDequantizeOp(np.array([0, 128, 255]), 0.0, 123.456, dtypes.quint8)
self._testDequantizeOp(
    np.array([0, 4, 42, 108, 243]), 5.0, 200.2, dtypes.quint8)
