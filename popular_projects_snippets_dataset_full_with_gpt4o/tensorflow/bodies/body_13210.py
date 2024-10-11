# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Match dtype of IndexedSlices.indices in outputs of branch_graphs."""
assert branch_graphs
# Indices of `IndexedSlices.indices` tensors in `branch_graphs[i].outputs`.
indexed_slice_indices = []
current_index = 0
# Note that this still contains Nones. We leave those in so that error
# messages contain the correct indices. We handle the Nones later when
# updating `current_index`.
branch_outputs_flat_with_composites = [
    nest.flatten(branch_graph.structured_outputs, expand_composites=False)
    for branch_graph in branch_graphs
]
outs_per_branch = [len(outs) for outs in branch_outputs_flat_with_composites]
assert len(set(outs_per_branch)) == 1, outs_per_branch
# Store indices of IndexedSlices.indices in `indexed_slice_indices`.
for output_idx, branch_outs in enumerate(
    zip(*branch_outputs_flat_with_composites)):
    if len(
        set(
            isinstance(out, indexed_slices.IndexedSlices)
            for out in branch_outs)) != 1:
        raise TypeError("Cannot reconcile tf.{op_name} {output_idx}-th outputs:\n"
                        "  branches returned: {outputs}".format(
                            op_name="cond" if op_type == _COND else "switch_case",
                            output_idx=output_idx,
                            outputs=branch_outs))
    if isinstance(branch_outs[0], indexed_slices.IndexedSlices):
        # indices is the second component of the composite tensor.
        indexed_slice_indices.append(current_index + 1)
    if nest.is_nested_or_composite(branch_outs[0]):
        current_index += len(nest.flatten(branch_outs[0], expand_composites=True))
    elif branch_outs[0] is not None:
        # `FuncGraph.outputs` does not contain Nones so no need to update the
        # counter in that case.
        current_index += 1

if not indexed_slice_indices:
    exit()

# `FuncGraph.outputs` is the flattened `FuncGraph.structured_outputs` minus
# the Nones.
if current_index != len(branch_graphs[0].outputs):
    raise ValueError("Insufficient elements in branch_graphs[0].outputs.\n"
                     "Expected: %i\n"
                     "Actual: %i" %
                     (current_index, len(branch_graphs[0].outputs)))

# Cast indices with mismatching types to int64.
for index in indexed_slice_indices:
    if any(bg.outputs[index].dtype not in (dtypes.int32, dtypes.int64)
           for bg in branch_graphs):
        raise TypeError("Type of IndexedSlices.indices must be int32 or int64. "
                        "Found: %s" %
                        str([bg.outputs[index].dtype for bg in branch_graphs]))
    if len(set(bg.outputs[index].dtype for bg in branch_graphs)) != 1:
        for branch_graph in branch_graphs:
            if branch_graph.outputs[index].dtype == dtypes.int32:
                with branch_graph.as_default():
                    branch_graph.outputs[index] = math_ops.cast(
                        branch_graph.outputs[index], dtypes.int64)

for branch_graph in branch_graphs:
    branch_graph.structured_outputs = _pack_sequence_as(
        branch_graph.structured_outputs, branch_graph.outputs)
