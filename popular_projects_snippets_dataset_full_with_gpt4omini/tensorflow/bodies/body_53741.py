# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for a function in a with_eager_op_as_function enabled test class.

  Blocks the function from being run with eager_op_as_function enabled.

  Args:
    unused_msg: Reason for disabling.

  Returns:
    The wrapped function with _disable_eager_op_as_function attr set to True.
  """
exit(_disable_test(execute_func=False))
