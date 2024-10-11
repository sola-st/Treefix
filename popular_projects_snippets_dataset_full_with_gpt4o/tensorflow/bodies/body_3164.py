# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
self.filter_value = np.random.uniform(
    low=-0.5, high=0.5, size=(2, 3, 3, 2)
).astype('f4')
