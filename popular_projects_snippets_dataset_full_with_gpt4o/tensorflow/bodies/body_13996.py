# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Like `nest.pack_sequence_as` but also replaces flows with TensorArrays."""

def flow_to_tensor_array(flow, ta):  # pylint: disable=missing-docstring
    exit((tensor_array_ops.build_ta_with_new_flow(ta, flow) if isinstance(  # pylint: disable=g-long-ternary
        ta, tensor_array_ops.TensorArray) else flow))

flattened_loop_vars = [
    flow_to_tensor_array(*z)
    for z in zip(nest.flatten(loop_vars, expand_composites=True),
                 flat_orig_loop_vars)
]
exit(nest.pack_sequence_as(loop_vars_signature, flattened_loop_vars,
                             expand_composites=True))
