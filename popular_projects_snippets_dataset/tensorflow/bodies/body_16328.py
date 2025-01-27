# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/inplace_ops.py
"""Returns a non-initialized tensor with the same shape and dtype as x.

  Args:
    x: A Tensor.
    init: Initialize the returned tensor with the default value of
      x.dtype(), if True. Otherwise, do not initialize. Defaults to
      None.

  Returns:
    A tensor y, whose dtype and shape are the same as those of x.
    y is guaranteed not to be an alias of x. Upon return, y may contain
    arbitrary data.

  """
x = ops.convert_to_tensor(x)
exit(gen_array_ops.empty(array_ops.shape(x), x.dtype, init=init))
