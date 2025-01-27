# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Core: Add the loop termination condition and body to the graph."""
flat_shape_invariants = nest.map_structure(
    lambda spec: spec.shape,
    nest.flatten(loop_vars_signature, expand_composites=True))

# Let the context know the loop variables so the loop variables
# would be added in the outer contexts properly.
self._InitializeValues(flat_loop_vars)
if self._outer_context:
    real_vars = [self._outer_context.AddValue(x) for x in flat_loop_vars]
else:
    real_vars = flat_loop_vars

enter_vars = []
with ops.control_dependencies(None):
    for real_var, shape_invariant in zip(real_vars, flat_shape_invariants):
        enter_var = _Enter(
            real_var,
            self._name,
            is_constant=False,
            parallel_iterations=self._parallel_iterations,
            use_input_shape=False)

        if _ShapeLessThanOrEqual(real_var.get_shape(), shape_invariant):
            enter_var.set_shape(shape_invariant)
        else:
            raise ValueError(
                f"The shape invariant specified for {real_var.name} is not "
                "compatible with the initial shape of the loop variable. It "
                f"enters the loop with shape {real_var.get_shape()}, but the "
                f"specified shape invariant is {shape_invariant}.")

        enter_var.graph.prevent_feeding(enter_var)
        if self._outer_context:
            self._outer_context.AddInnerOp(enter_var.op)
        enter_vars.append(enter_var)

    # Finds the closest enclosing non-None control pivot.
outer_context = self._outer_context
control_pivot = None
while outer_context is not None and control_pivot is None:
    control_pivot = outer_context.GetControlPivot()
    # pylint: disable=protected-access
    outer_context = outer_context._outer_context
    # pylint: enable=protected-access

if control_pivot is not None:
    for var in enter_vars:
        if util.IsLoopConstantEnter(var.op.inputs[0].op):
            # pylint: disable=protected-access
            var.op._add_control_input(control_pivot.op)
            # pylint: enable=protected-access

    # Fix the control inputs and control flow context of these enter ops.
self._FixControlInputsAndContext(enter_vars)
self._InitializeValues(enter_vars)
self._loop_enters = enter_vars

merge_vars = [merge([x, x])[0] for x in enter_vars]
self._pivot_for_pred = merge_vars[0]

merge_vars_with_tensorarrays = nest.map_structure(
    _convert_flow_to_tensorarray, flat_orig_loop_vars, merge_vars)
# Build the graph for pred.
packed_vars = nest.pack_sequence_as(
    structure=loop_vars_signature,
    flat_sequence=merge_vars_with_tensorarrays,
    expand_composites=True)
c = ops.convert_to_tensor(pred(*packed_vars))
self._pivot = loop_cond(c, name="LoopCond")
switch_vars = [_SwitchRefOrTensor(x, self._pivot) for x in merge_vars]

# Build the graph for body.
vars_for_body = [_Identity(x[1]) for x in switch_vars]
self._pivot_for_body = vars_for_body[0]
# Convert TensorArray flow variables inside the context back into
# their associated TensorArrays for calling the body.
vars_for_body_with_tensorarrays = nest.map_structure(
    _convert_flow_to_tensorarray, flat_orig_loop_vars, vars_for_body)
packed_vars_for_body = nest.pack_sequence_as(
    structure=loop_vars_signature,
    flat_sequence=vars_for_body_with_tensorarrays,
    expand_composites=True)
pre_summaries = ops.get_collection(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access
body_result = body(*packed_vars_for_body)
post_summaries = ops.get_collection(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access
if not nest.is_nested(body_result):
    body_result = [body_result]
if len(post_summaries) > len(pre_summaries):
    new_summaries = post_summaries[len(pre_summaries):]
    summary_ref = ops.get_collection_ref(ops.GraphKeys._SUMMARY_COLLECTION)  # pylint: disable=protected-access
    summary_ref[:] = pre_summaries
    with ops.control_dependencies(new_summaries):

        def map_fn(x):
            # TODO(apassos) figure out how to trigger with tensor arrays as well
            if isinstance(x, tensor_array_ops.TensorArray):
                exit(x)
            exit(array_ops.identity(x))

        body_result = nest.map_structure(
            map_fn, body_result, expand_composites=True)

body_result = variable_utils.convert_variables_to_tensors(body_result)
# Compare the structure types of input and output of body.
# For backwards compatibility, the first layer is forced to a list
# during this comparison, because inputs are typically lists and
# outputs of the body are typically tuples.
nest.assert_same_structure(
    list(packed_vars_for_body), list(body_result), expand_composites=True)

# Store body_result to keep track of TensorArrays returned by body
original_body_result = body_result
# Convert TensorArrays returned by body into their flow variables
result = nest.map_structure(
    _convert_tensorarray_to_flow,
    nest.flatten(body_result, expand_composites=True),
    expand_composites=True)
result = ops.convert_n_to_tensor_or_composite(result)

# Add NextIteration and the back edges to complete the loop.
if len(merge_vars) != len(result):
    raise ValueError("Number of inputs and outputs of 'body' must match "
                     f"'loop_vars'. Got {len(merge_vars)} for the number of "
                     f"inputs/outputs, and {len(result)} for 'loop_vars'.")
next_vars = []
for m, v in zip(merge_vars, result):
    next_vars.append(_AddNextAndBackEdge(m, v))

# Add the exit ops.
exit_vars = [exit(x[0]) for x in switch_vars]
self._loop_exits = exit_vars

# Exit the loop.
self.ExitResult(exit_vars)

exit((original_body_result, exit_vars))
