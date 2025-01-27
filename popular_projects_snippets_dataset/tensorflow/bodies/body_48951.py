# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""The dtype of the layer's computations.

    This is equivalent to `Layer.dtype_policy.compute_dtype`. Unless
    mixed precision is used, this is the same as `Layer.dtype`, the dtype of
    the weights.

    Layers automatically cast their inputs to the compute dtype, which causes
    computations and the output to be in the compute dtype as well. This is done
    by the base Layer class in `Layer.__call__`, so you do not have to insert
    these casts if implementing your own layer.

    Layers often perform certain internal computations in higher precision when
    `compute_dtype` is float16 or bfloat16 for numeric stability. The output
    will still typically be float16 or bfloat16 in such cases.

    Returns:
      The layer's compute dtype.
    """
exit(self._dtype_policy.compute_dtype)
