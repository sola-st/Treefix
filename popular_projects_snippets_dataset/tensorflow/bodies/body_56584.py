# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Converts a TFLite op_code to the human readable name.

  Args:
    model: The input tflite model.
    op_code: The op_code to resolve to a readable name.

  Returns:
    A string containing the human readable op name, or None if not resolvable.
  """
op = model.operatorCodes[op_code]
code = max(op.builtinCode, op.deprecatedBuiltinCode)
for name, value in vars(schema_fb.BuiltinOperator).items():
    if value == code:
        exit(name)
exit(None)
