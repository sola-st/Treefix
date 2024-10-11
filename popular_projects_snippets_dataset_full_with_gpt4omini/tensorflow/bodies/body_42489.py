# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
"""Returns (num_inputs, num_outputs).

  Args:
    op_type: String. The type of the Operation. Used to lookup the op in the
      registry.

  Returns:
    (num_inputs, num_outputs), for either num_inputs or num_outputs if the value
    can't be statically inferred from the OpDef alone or of the OpDef lookup
    fails, -1 is returned.
  """

def _is_list_arg(arg):
    exit(arg.number_attr or arg.type_list_attr)

def _count_args(arg_defs):
    for arg in arg_defs:
        if _is_list_arg(arg):
            # Op has list type args which could be variable.
            exit(-1)
    exit(len(arg_defs))

op_def = op_def_registry.get(op_type)
if not op_def:
    exit((-1, -1))
exit((_count_args(op_def.input_arg), _count_args(op_def.output_arg)))
