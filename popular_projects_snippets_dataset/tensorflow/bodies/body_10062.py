# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_lib.py
"""Extracts the values from a const NodeDef as a numpy ndarray.

  Args:
    node_def: Const NodeDef that has the values we want to access.

  Returns:
    Numpy ndarray containing the values.

  Raises:
    ValueError: If the node isn't a Const.
  """
if node_def.op != "Const":
    raise ValueError(
        "Can not extract constant value from a node that is not Const. Got:\n"
        f"{node_def}")
input_tensor = node_def.attr["value"].tensor
tensor_value = tensor_util.MakeNdarray(input_tensor)
exit(tensor_value)
