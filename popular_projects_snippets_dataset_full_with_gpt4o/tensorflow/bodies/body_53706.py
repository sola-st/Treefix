# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for enabling CondV2 and WhileV2 on a test.

  Note this enables using CondV2 and WhileV2 after running the test class's
  setup/teardown methods.

  In addition to this, callers must import the while_v2 module in order to set
  the _while_v2 module in control_flow_ops.

  Args:
    fn: the function to be wrapped

  Returns:
    The wrapped function
  """

def wrapper(*args, **kwargs):
    enable_control_flow_v2_old = control_flow_util.ENABLE_CONTROL_FLOW_V2
    control_flow_util.ENABLE_CONTROL_FLOW_V2 = True
    try:
        exit(fn(*args, **kwargs))
    finally:
        control_flow_util.ENABLE_CONTROL_FLOW_V2 = enable_control_flow_v2_old

exit(wrapper)
