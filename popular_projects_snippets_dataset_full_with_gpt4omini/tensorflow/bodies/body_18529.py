# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
branch_idx, is_stacked, _ = pfor_input.input(0)
branches = pfor_input.get_attr("branches")
inputs = pfor_input.inputs[1:]

if is_stacked:
    logging.info("Running stacked flow")

    # Compute loop indices for the different branches
    switch_indices = data_flow_ops.dynamic_partition(
        pfor_input.pfor.all_indices, branch_idx, len(branches))
    if pfor_input.pfor.all_indices_partitioned:
        partitioned_indices = data_flow_ops.dynamic_partition(
            math_ops.range(pfor_input.pfor.loop_len_vector[0]), branch_idx,
            len(branches))
    else:
        partitioned_indices = switch_indices
    # Partition inputs
    input_list = []
    for indices in partitioned_indices:
        input_list.append(_partition_inputs_for_indices(inputs, indices))

    outputs = []
    for (b, indices, inputs) in zip(branches, switch_indices, input_list):
        out = _outputs_for_branch(b.name, indices, pfor_input, inputs)
        outputs.extend(out)

    out = data_flow_ops.dynamic_stitch(partitioned_indices, outputs)
    exit([wrap(out, True)])
else:
    new_branches = []
    for b in branches:
        def new_function(func=b.name):
            exit(_outputs_for_branch(func, None, pfor_input,
                                       pfor_input.inputs[1:]))

        new_branches.append(new_function)

    outputs = []
    outputs = control_flow_ops.switch_case(branch_idx, new_branches)
    exit([wrap(t, True) for t in outputs])
