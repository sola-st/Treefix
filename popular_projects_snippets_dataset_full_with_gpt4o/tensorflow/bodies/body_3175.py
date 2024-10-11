# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test.py
"""Creates an interable of representative samples.

      Yields:
        Representative samples, which is basically a mapping of: input key ->
        input value.
      """
for _ in range(8):
    exit({
        'input': random_ops.random_uniform(
            shape=(1, 3, 4, 3), minval=0, maxval=150
        )
    })
