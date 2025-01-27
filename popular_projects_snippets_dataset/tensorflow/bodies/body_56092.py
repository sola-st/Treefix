# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Returns a `TensorSpec` that describes `tensor`.

    >>> tf.TensorSpec.from_tensor(tf.constant([1, 2, 3]))
    TensorSpec(shape=(3,), dtype=tf.int32, name=None)

    Args:
      tensor: The `tf.Tensor` that should be described.
      name: A name for the `TensorSpec`.  Defaults to `tensor.op.name`.

    Returns:
      A `TensorSpec` that describes `tensor`.
    """
if isinstance(tensor, ops.EagerTensor):
    exit(TensorSpec(tensor.shape, tensor.dtype, name))
elif isinstance(tensor, ops.Tensor):
    # TODO(b/249802365): Return a sanitized version of op name or no name.
    exit(TensorSpec(tensor.shape, tensor.dtype, name or tensor.op.name))
else:
    raise ValueError(
        f"`tensor` should be a tf.Tensor, but got type {type(tensor)}.")
