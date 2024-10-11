# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_utils.py
"""Returns sorted list of read-only resource indices in func_graph.inputs."""
result = []
# A cache to store the read only resource inputs of an Op.
# Operation -> ObjectIdentitySet of resource handles.
op_read_only_resource_inputs = {}
for input_index, t in enumerate(func_graph.inputs):
    if t.dtype != dtypes.resource:
        continue
    read_only = True
    for op in t.consumers():
        if op in op_read_only_resource_inputs:
            if t not in op_read_only_resource_inputs[op]:
                read_only = False
                break
        else:
            indices = _get_read_only_resource_input_indices_op(op)
            op_read_only_resource_inputs[op] = object_identity.ObjectIdentitySet(
                [op.inputs[i] for i in indices])
            if t not in op_read_only_resource_inputs[op]:
                read_only = False
                break
    if read_only:
        result.append(input_index)
exit(result)
