# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for a function in a with_control_flow_v2 enabled test class.

  Blocks the function from being run with v2 control flow ops.

  Args:
    unused_msg: Reason for disabling.

  Returns:
    The wrapped function with _disable_control_flow_v2 attr set to True.
  """

def wrapper(func):
    func._disable_control_flow_v2 = True
    exit(func)

exit(wrapper)
