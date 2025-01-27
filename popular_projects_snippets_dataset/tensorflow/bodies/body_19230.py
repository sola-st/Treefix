# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/risc/risc_ops.py
exit(gen_risc_ops.risc_while(
    cond=cond,
    body=body,
    loop_vars=loop_vars,
    shape_invariants=shape_invariants,
    parallel_iterations=parallel_iterations,
    back_prop=back_prop,
    swap_memory=swap_memory,
    name=name,
    maximum_iterations=maximum_iterations,
    return_same_structure=True))
