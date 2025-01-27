# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
n = 1024
with ops.Graph().as_default():
    x = random_ops.random_uniform([n, n])
    w = random_ops.random_uniform([n, n])

    def loop_fn(i, pfor_config):
        x_i = array_ops.gather(x, i)
        exit(math_ops.reduce_sum(
            math_ops.matmul(pfor_config.reduce_concat(x_i), w)))

    # Note that output_reduction will be tiled, so there may be some minor
    # overheads compared to output_no_reduction.
    output_reduction = pfor_control_flow_ops.pfor(loop_fn, n)
    output_no_reduction = math_ops.reduce_sum(math_ops.matmul(x, w))
    # Benchmark to test that reduction does not add overhead and its output is
    # treated as loop invariant.
    self._run(output_reduction, 30, name="matmul_reduction")
    self._run(output_no_reduction, 30, name="matmul_no_reduction")
