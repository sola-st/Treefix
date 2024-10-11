# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays_test.py
self._testBinOp([3, 5], [2, 4],
                ops.convert_to_tensor(value=[1.5, 1.25]),
                lambda a, b: b.__rtruediv__(a),
                types=self._truediv_types)
