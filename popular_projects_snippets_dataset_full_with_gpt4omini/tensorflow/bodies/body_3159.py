# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
self._bias = bias
self._kernel = np.random.uniform(size=y_shape).astype('f4')
self._min = (-0.8, -0.8, -0.9)
self._max = (0.9, 0.9, 1.0)
