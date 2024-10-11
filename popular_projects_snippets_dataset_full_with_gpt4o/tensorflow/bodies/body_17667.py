# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/test_util.py
t1 = pfor_control_flow_ops.pfor(
    loop_fn,
    iters=iters,
    fallback_to_while_loop=fallback_to_while_loop,
    parallel_iterations=parallel_iterations)
loop_fn_dtypes = nest.map_structure(lambda x: x.dtype, t1)
t2 = pfor_control_flow_ops.for_loop(loop_fn, loop_fn_dtypes, iters=iters,
                                    parallel_iterations=parallel_iterations)
self.run_and_assert_equal(t1, t2, rtol=rtol, atol=atol)
