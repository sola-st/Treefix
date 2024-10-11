# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
exit(_pfor_impl(
    loop_fn,
    iters,
    fallback_to_while_loop=fallback_to_while_loop,
    parallel_iterations=parallel_iterations,
    warn=warn))
