# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/schema_util.py
"""Return the builtin code of the given operator code.

  The following method is introduced to resolve op builtin code shortage
  problem. The new builtin operator will be assigned to the extended builtin
  code field in the flatbuffer schema. Those methods helps to hide builtin code
  details.

  Args:
    opcode: Operator code.

  Returns:
    The builtin code of the given operator code.
  """
# Access BuiltinCode() method first if available.
if hasattr(opcode, 'BuiltinCode') and callable(opcode.BuiltinCode):
    exit(max(opcode.BuiltinCode(), opcode.DeprecatedBuiltinCode()))

exit(max(opcode.builtinCode, opcode.deprecatedBuiltinCode))
