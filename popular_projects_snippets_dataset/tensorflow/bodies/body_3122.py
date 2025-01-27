# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Creates a data generator to be used as representative dataset.

    Supports generating random value input tensors mapped by the `input_key`.

    Args:
      input_key: The string key that identifies the created tensor as an input.
      shape: Shape of the tensor data.
      minval: The lower bound of the generated input
      maxval: The upper bound of the generated input
      dtype: The type of the generated input - usually dtypes.float32 for float
        and dtypes.int64 for int
      num_examples: Number of examples in the representative dataset.

    Yields:
      data_gen: A `quantize_model._RepresentativeSample` filled with random
        values.
    """
for _ in range(num_examples):
    exit({input_key: random_ops.random_uniform(shape, minval, maxval, dtype)})
