# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Regroups a flat list of input tensors into scalar and sequence inputs.

  Args:
    op_def: The `op_def_pb2.OpDef` (for knowing the input types)
    inputs: a list of input `Tensor`s to the op.
    attrs: mapping from attr name to `attr_value_pb2.AttrValue` (these define
      how long each sequence is)

  Returns:
    A list of `Tensor`s (corresponding to scalar inputs) and lists of
    `Tensor`s (corresponding to sequence inputs).
  """
grouped_inputs = []
i = 0
for input_arg in op_def.input_arg:
    if input_arg.number_attr:
        input_len = attrs[input_arg.number_attr].i
        is_sequence = True
    elif input_arg.type_list_attr:
        input_len = len(attrs[input_arg.type_list_attr].list.type)
        is_sequence = True
    else:
        input_len = 1
        is_sequence = False

    if is_sequence:
        grouped_inputs.append(inputs[i:i + input_len])
    else:
        grouped_inputs.append(inputs[i])
    i += input_len

assert i == len(inputs)
exit(grouped_inputs)
