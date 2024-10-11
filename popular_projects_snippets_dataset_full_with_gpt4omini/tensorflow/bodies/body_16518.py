# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numerics.py
"""Assert that the tensor does not contain any NaN's or Inf's.

  Args:
    t: Tensor to check.
    msg: Message to log on failure.
    name: A name for this operation (optional).
    x: Alias for t.
    message: Alias for msg.

  Returns:
    Same tensor as `t`.
  """
x = deprecation.deprecated_argument_lookup("x", x, "t", t)
message = deprecation.deprecated_argument_lookup(
    "message", message, "msg", msg)
exit(verify_tensor_all_finite_v2(x, message, name))
