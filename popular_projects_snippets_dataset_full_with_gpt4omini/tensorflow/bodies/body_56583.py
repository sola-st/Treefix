# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Rename custom ops so they use the same naming style as builtin ops.

  Args:
    model: The input tflite model.
    map_custom_op_renames: A mapping from old to new custom op names.
  """
for op_code in model.operatorCodes:
    if op_code.customCode:
        op_code_str = op_code.customCode.decode('ascii')
        if op_code_str in map_custom_op_renames:
            op_code.customCode = map_custom_op_renames[op_code_str].encode('ascii')
