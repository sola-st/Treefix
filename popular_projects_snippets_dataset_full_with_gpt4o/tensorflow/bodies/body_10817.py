# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add the loop termination condition and body to the graph."""

# Keep flat_orig_loop_vars to identify which are TensorArrays
flat_orig_loop_vars = nest.flatten(loop_vars, expand_composites=True)

loop_vars = nest.map_structure(
    _convert_to_tensor_or_composite_or_tensorarray, loop_vars)
# Convert TensorArrays to their flow variables
flat_loop_vars = nest.map_structure(
    _convert_tensorarray_to_flow,
    nest.flatten(loop_vars, expand_composites=True))

if shape_invariants is not None:
    loop_vars_signature = nest.map_structure(
        _shape_invariant_to_type_spec, loop_vars, shape_invariants)
else:
    loop_vars_signature = nest.map_structure(
        _shape_invariant_to_type_spec, loop_vars)

try:
    self.Enter()
    # _BuildLoop calls _update_input in several places. _mutation_lock()
    # ensures a Session.run call cannot occur between creating and mutating
    # new ops.
    with ops.get_default_graph()._mutation_lock():  # pylint: disable=protected-access
        original_body_result, exit_vars = self._BuildLoop(
            pred, body, flat_orig_loop_vars, flat_loop_vars,
            loop_vars_signature)
finally:
    self.Exit()

flat_result = nest.flatten(original_body_result, expand_composites=True)
# Convert TensorArray flow variables outside the context back into
# their associated TensorArrays for returning to caller.
exit_vars_with_tensorarrays = nest.map_structure(
    _convert_flow_to_tensorarray, flat_result, exit_vars)

packed_exit_vars = nest.pack_sequence_as(
    structure=original_body_result,
    flat_sequence=exit_vars_with_tensorarrays,
    expand_composites=True)

if return_same_structure:
    exit(packed_exit_vars)
else:
    exit(packed_exit_vars[0] if len(exit_vars) == 1 else packed_exit_vars)
