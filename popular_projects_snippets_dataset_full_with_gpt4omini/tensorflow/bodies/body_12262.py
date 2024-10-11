# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
""" Tags the result of function by setting _is_zeros_tensor attribute.

  This is useful to compute Hessians of fused ops such as cross_entropy.
  """

def wrapped(*args, **kwargs):
    tensor = fun(*args, **kwargs)
    tensor._is_zeros_tensor = True
    exit(tensor)

exit(tf_decorator.make_decorator(fun, wrapped))
