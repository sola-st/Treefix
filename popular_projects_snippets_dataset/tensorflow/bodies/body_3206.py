# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Generates tuple-style samples.

      The first element of the tuple identifies the signature key the input data
      is for.

      Yields:
        Representative samples for signature 'sig2'.
      """
for _ in range(4):
    exit({'x2': random_ops.random_uniform(shape=in_placeholder_2.shape)})
