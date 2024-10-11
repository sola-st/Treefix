# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Decorator that adds docstring to the function for symbol `sym`.

    Args:
      func: Function for a TensorFlow op

    Returns:
      A version of `func` with documentation attached.
    """

func.__doc__ = """
    Assert the condition `x {sym} y` holds element-wise.

    This Op checks that `x[i] {sym} y[i]` holds for every pair of (possibly
    broadcast) elements of `x` and `y`. If both `x` and `y` are empty, this is
    trivially satisfied.

    If `x` {sym} `y` does not hold, `message`, as well as the first `summarize`
    entries of `x` and `y` are printed, and `InvalidArgumentError` is raised.

    When using inside `tf.function`, this API takes effects during execution.
    It's recommended to use this API with `tf.control_dependencies` to
    ensure the correct execution order.

    In the following example, without `tf.control_dependencies`, errors may
    not be raised at all.
    Check `tf.control_dependencies` for more details.

    >>> def check_size(x):
    ...   with tf.control_dependencies([
    ...       tf.debugging.{opname}(tf.size(x), {test_var},
    ...                       message='Bad tensor size')]):
    ...     return x

    >>> check_size(tf.ones([2, 3], tf.float32))
    Traceback (most recent call last):
       ...
    InvalidArgumentError: ...

    Args:
      x:  Numeric `Tensor`.
      y:  Numeric `Tensor`, same dtype as and broadcastable to `x`.
      message: A string to prefix to the default message. (optional)
      summarize: Print this many entries of each tensor. (optional)
      name: A name for this operation (optional).  Defaults to "{opname}".

    Returns:
      Op that raises `InvalidArgumentError` if `x {sym} y` is False. This can
        be used with `tf.control_dependencies` inside of `tf.function`s to
        block followup computation until the check has executed.
      @compatibility(eager)
      returns None
      @end_compatibility

    Raises:
      InvalidArgumentError: if the check can be performed immediately and
        `x == y` is False. The check can be performed immediately during eager
        execution or if `x` and `y` are statically known.
    """.format(
    sym=sym, opname=opname, test_var=test_var)
exit(func)
