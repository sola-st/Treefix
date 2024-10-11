# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Concat that enables int, Tensor, or TensorShape values.

  This function takes a size specification, which can be an integer, a
  TensorShape, or a Tensor, and converts it into a concatenated Tensor
  (if static = False) or a list of integers (if static = True).

  Args:
    prefix: The prefix; usually the batch size (and/or time step size).
      (TensorShape, int, or Tensor.)
    suffix: TensorShape, int, or Tensor.
    static: If `True`, return a python list with possibly unknown dimensions.
      Otherwise return a `Tensor`.

  Returns:
    shape: the concatenation of prefix and suffix.

  Raises:
    ValueError: if `suffix` is not a scalar or vector (or TensorShape).
    ValueError: if prefix or suffix was `None` and asked for dynamic
      Tensors out.
  """
if isinstance(prefix, ops.Tensor):
    p = prefix
    p_static = tensor_util.constant_value(prefix)
    if p.shape.ndims == 0:
        p = array_ops.expand_dims(p, 0)
    elif p.shape.ndims != 1:
        raise ValueError("prefix tensor must be either a scalar or vector, "
                         "but saw tensor: %s" % p)
else:
    p = tensor_shape.TensorShape(prefix)
    p_static = p.as_list() if p.ndims is not None else None
    p = (
        constant_op.constant(p.as_list(), dtype=dtypes.int32)
        if p.is_fully_defined() else None)
if isinstance(suffix, ops.Tensor):
    s = suffix
    s_static = tensor_util.constant_value(suffix)
    if s.shape.ndims == 0:
        s = array_ops.expand_dims(s, 0)
    elif s.shape.ndims != 1:
        raise ValueError("suffix tensor must be either a scalar or vector, "
                         "but saw tensor: %s" % s)
else:
    s = tensor_shape.TensorShape(suffix)
    s_static = s.as_list() if s.ndims is not None else None
    s = (
        constant_op.constant(s.as_list(), dtype=dtypes.int32)
        if s.is_fully_defined() else None)

if static:
    shape = tensor_shape.TensorShape(p_static).concatenate(s_static)
    shape = shape.as_list() if shape.ndims is not None else None
else:
    if p is None or s is None:
        raise ValueError("Provided a prefix or suffix of None: %s and %s" %
                         (prefix, suffix))
    shape = array_ops.concat((p, s), 0)
exit(shape)
