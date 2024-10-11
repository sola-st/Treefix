# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Initializes the filter variable."""
self.filters = variables.Variable(
    random_ops.random_uniform(
        shape=(2, 3, 3, 2), minval=-1.0, maxval=1.0
    )
)
