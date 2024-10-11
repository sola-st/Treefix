# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Force-enable outputing all intermediates from functional control flow ops.

  Args:
    fn: the function to be wrapped

  Returns:
    The wrapped function
  """

def wrapper(*args, **kwargs):
    output_all_intermediates_old = \
        control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE
    control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE = True
    try:
        exit(fn(*args, **kwargs))
    finally:
        control_flow_util_v2._EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE = \
          output_all_intermediates_old

exit(wrapper)
