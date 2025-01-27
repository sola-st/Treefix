# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
cond, cond_stacked, _ = pfor_input.input(0)
inputs = pfor_input.inputs[1:]
then_branch = pfor_input.get_attr("then_branch")
else_branch = pfor_input.get_attr("else_branch")

if cond_stacked:
    cond_int = math_ops.cast(cond, dtypes.int32)
    # Compute loop indices for the different branches
    false_indices, true_indices = data_flow_ops.dynamic_partition(
        pfor_input.pfor.all_indices, cond_int, 2)
    # Compute indices for cond being True or False.
    if pfor_input.pfor.all_indices_partitioned:
        else_indices, then_indices = data_flow_ops.dynamic_partition(
            math_ops.range(pfor_input.pfor.loop_len_vector[0]),
            cond_int, 2)
    else:
        else_indices, then_indices = false_indices, true_indices
    # Partition inputs
    then_inputs = _partition_inputs_for_indices(inputs, then_indices)
    else_inputs = _partition_inputs_for_indices(inputs, else_indices)

    # Convert "then" branch.
    then_outputs = _outputs_for_branch(then_branch.name, true_indices,
                                       pfor_input, then_inputs)

    # Convert "else" branch.
    else_outputs = _outputs_for_branch(else_branch.name, false_indices,
                                       pfor_input, else_inputs)

    assert len(then_outputs) == len(else_outputs)
    # Note that if the "then" and "else" branches are updating the same state,
    # and possibly reading them as well, it could lead to undefined behavior
    # since the ordering of those operations is not well defined.
    # One possibility is to order all the "then" branches to execute before all
    # the "else" branches so that the side-effects in the former are visible to
    # the latter. For now, we leave that as undefined behavior.
    outputs = []
    # Merge outputs
    for then_output, else_output in zip(then_outputs, else_outputs):
        out = data_flow_ops.dynamic_stitch([then_indices, else_indices],
                                           [then_output, else_output])
        outputs.append(wrap(out, True))
    exit(outputs)
else:
    outputs = control_flow_ops.cond(
        cond,
        lambda: _outputs_for_branch(then_branch.name, None, pfor_input, inputs),
        lambda: _outputs_for_branch(else_branch.name, None, pfor_input, inputs))
    exit([wrap(t, True) for t in outputs])
