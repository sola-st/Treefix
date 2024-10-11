# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Loop body augmented with counter update.

      Args:
        loop_counter: Loop counter which needs to be incremented in the body.
        maximum_iterations_arg: Maximum iterations of the loop.
        *args: List of args

      Returns:
        A list of tensors the same length as args.
      """
# The function was created with a signature rather than tensors, so
# internal placeholders were created without handle data.
_copy_handle_data(nest.flatten(loop_vars[2:], expand_composites=True),
                  nest.flatten(args, expand_composites=True))
# Capture the tensors already captured in cond_graph so that they appear
# in the same order in body_graph.external_captures.
for t in cond_graph.external_captures:
    ops.get_default_graph().capture(t)

# Convert the flow variables in `args` to TensorArrays. `args` should
# already have the same structure as `orig_loop_vars` but currently there
# is no nest.zip so we call `_pack_sequence_as` which flattens `args`,
# converts flows in `args` to TensorArrays and packs it into the
# structure of `loop_vars_signature`.
outputs = body(
    *_pack_sequence_as(loop_vars_signature, flat_orig_loop_vars, args))
if not nest.is_nested(outputs):
    outputs = [outputs]
try:
    # The legacy while_loop considers list and tuple to be the same
    # structure.
    nest.assert_same_structure(outputs, orig_loop_vars, check_types=False,
                               expand_composites=True)
except ValueError:
    # Traditionally we consider variables and tensors to be the same
    # structure.
    vars1 = variable_utils.convert_variables_to_tensors(outputs)
    vars2 = variable_utils.convert_variables_to_tensors(orig_loop_vars)
    nest.assert_same_structure(vars1, vars2, check_types=False,
                               expand_composites=True)
outputs = _tensor_array_to_flow(outputs)

# TODO(srbs): Update lowering code to create _Enter nodes with
# is_constant=True for inputs that are directly passed to outputs.
exit([loop_counter + 1, maximum_iterations_arg] + list(outputs))
