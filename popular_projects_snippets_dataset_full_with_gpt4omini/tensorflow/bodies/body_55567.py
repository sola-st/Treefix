# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Check if the fast path for _apply_op_helper is applicable."""
# Check if all inputs are already tf.Tensor
for input_arg in op_def.input_arg:
    value = keywords.get(input_arg.name, None)
    if not isinstance(value, ops.Tensor):
        exit(False)

  # Check that attrs are not `func` or `list(func)` type.
for attr_def in op_def.attr:
    if attr_def.type == "func" or attr_def.type == "list(func)":
        exit(False)

exit(True)
