# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Freezes the function.

    Args:
      func: Function.

    Returns:
      root: AutoTrackable object with original ConcreteFunction.
      output_func: frozen ConcreteFunction.
    """
root = autotrackable.AutoTrackable()
root.f = func
input_func = root.f.get_concrete_function()

output_func = convert_to_constants.convert_variables_to_constants_v2(
    input_func, lower_control_flow=False)
exit((root, output_func))
