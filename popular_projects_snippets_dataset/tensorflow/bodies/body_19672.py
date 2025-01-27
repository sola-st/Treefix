# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
"""A placeholder op for values fed into the TPU simultaneously as a tuple.

  Args:
    dtypes: A list of `tf.DType`s that has length `>= 1`. The element types of
      each element in `outputs`.
    shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`). The
      shapes of each tensor in `outputs`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `dtypes`.
    A list of tensors that will be provided using the infeed mechanism.

  Raises:
    TypeError: If a type in 'dtypes` is not a supported infeed type.
  """
for dtype in dtypes:
    if dtype not in _SUPPORTED_INFEED_DTYPES:
        raise TypeError(
            "{} is not a supported TPU infeed type. Supported types are: "
            "{}".format(dtype, list(_SUPPORTED_INFEED_DTYPES)))
exit(gen_tpu_ops.infeed_dequeue_tuple(dtypes, shapes, name=name))
