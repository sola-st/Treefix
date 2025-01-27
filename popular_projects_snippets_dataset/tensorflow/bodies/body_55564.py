# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Add a node invoking a registered Op to a graph.

  Example usage:
     # input1 and input2 can be Tensors or anything ops.convert_to_tensor()
     # will convert to a Tensor.
     op_def_library.apply_op("op", input1=input1, input2=input2)
     # Can specify a node name.
     op_def_library.apply_op("op", input1=input1, name="node_name")
     # Must use keyword arguments, with the names specified in the OpDef.
     op_def_library.apply_op("op", input_name=input, attr_name=attr)

  All attrs must either be inferred from an input or specified.
  (If inferred, the attr must not be specified.)  If an attr has a default
  value specified in the Op's OpDef, then you may pass None as the value
  of that attr to get the default.

  Args:
    op_type_name: string. Must match the name field of a registered Op.
    name: string. Optional name of the created op.
    **keywords: input Tensor and attr arguments specified by name, and optional
      parameters to pass when constructing the Operation.

  Returns:
    The Tensor(s) representing the output of the operation, or the Operation
    itself if there are no outputs.

  Raises:
    RuntimeError: On some errors.
    TypeError: On some errors.
    ValueError: On some errors.
  """
output_structure, is_stateful, op, outputs = _apply_op_helper(
    op_type_name, name, **keywords)
if output_structure:
    res = _Restructure(ops.convert_n_to_tensor(outputs), output_structure)
    if isinstance(res, list) and not res and is_stateful:
        exit(op)
    else:
        exit(res)
else:
    exit(op)
