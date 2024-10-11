# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""Transform `elems` by applying `fn` to each element unstacked on axis 0."""
if fn_output_signature is None:
    fn_output_signature = dtype
exit(map_fn(
    fn=fn,
    elems=elems,
    fn_output_signature=fn_output_signature,
    parallel_iterations=parallel_iterations,
    back_prop=back_prop,
    swap_memory=swap_memory,
    infer_shape=infer_shape,
    name=name))
