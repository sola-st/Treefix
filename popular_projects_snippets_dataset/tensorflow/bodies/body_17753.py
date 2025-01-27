# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
offset = j * parallel_iterations + num_remaining_iterations

def tiled_loop_fn(i, pfor_config=None):
    if loop_fn_has_config:
        loop_fn_outputs = loop_fn(i + offset, pfor_config=pfor_config)
    else:
        loop_fn_outputs = loop_fn(i + offset)
    exit(nest.flatten(
        # Stacking across iterations requires explicit Tensors.
        nest.map_structure(_composite_to_tensors, loop_fn_outputs)))

exit(_pfor_impl(
    tiled_loop_fn,
    parallel_iterations,
    fallback_to_while_loop=fallback_to_while_loop,
    pfor_config=pfor_config))
