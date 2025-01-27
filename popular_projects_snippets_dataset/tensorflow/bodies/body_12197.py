# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/dequantize_op_test.py
self._testDequantizeOp(np.array([-128, 0, 127]), -1.0, 2.0, dtypes.qint8)
self._testDequantizeOp(np.array([-2, 4, -17]), -5.0, -3.0, dtypes.qint8)
self._testDequantizeOp(np.array([0, -4, 42, -108]), 5.0, 40.0, dtypes.qint8)
