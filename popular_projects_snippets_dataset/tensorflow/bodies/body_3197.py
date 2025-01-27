# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Generates tuple-style samples for signature 'sig1'.

      The first element of the tuple identifies the signature key the input data
      is for.

      Yields:
        Representative sample for 'sig1'.
      """
for _ in range(4):
    exit({'matmul_input': random_ops.random_uniform(shape=(1, 4))})
