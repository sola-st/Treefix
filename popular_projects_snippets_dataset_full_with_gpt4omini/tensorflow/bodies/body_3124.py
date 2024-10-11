# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Initializes a SimpleGatherAndConvModel."""
embedding_w_val = np.random.randn(1024, 3, 4, 3).astype('f4')
self.embedding_w = embedding_w_val
