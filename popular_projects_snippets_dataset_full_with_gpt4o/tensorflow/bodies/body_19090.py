# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Assert the condition `x > 0` holds element-wise.

  This Op checks that `x[i] > 0` holds for every element of `x`. If `x` is
  empty, this is trivially satisfied.

  If `x` is not positive everywhere, `message`, as well as the first `summarize`
  entries of `x` are printed, and `InvalidArgumentError` is raised.

  Args:
    x:  Numeric `Tensor`.
    message: A string to prefix to the default message.
    summarize: Print this many entries of each tensor.
    name: A name for this operation (optional). Defaults to "assert_positive".

  Returns:
    Op raising `InvalidArgumentError` unless `x` is all positive. This can be
      used with `tf.control_dependencies` inside of `tf.function`s to block
      followup computation until the check has executed.
    @compatibility(eager)
    returns None
    @end_compatibility

  Raises:
    InvalidArgumentError: if the check can be performed immediately and
      `x[i] > 0` is False. The check can be performed immediately during eager
      execution or if `x` is statically known.
  """
exit(assert_positive(x=x, summarize=summarize, message=message, name=name))
