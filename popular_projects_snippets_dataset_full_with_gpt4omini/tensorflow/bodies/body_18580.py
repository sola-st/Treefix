# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
# The while_loop in this setup is similar to the one in test_stateless_while
# whose condition is loop variant. However here we wrap the cond and body of
# the loop in a way that makes the while_loop condition pfor loop invariant.
# This allows xla compilation to work since the vectorized code no longer
# needs to perform dynamic partitioning of the inputs.
x = random_ops.random_uniform([3, 5])
lengths = constant_op.constant([4, 0, 2])

def loop_fn(i, pfor_config):
    x_i = array_ops.gather(x, i)
    lengths_i = array_ops.gather(lengths, i)

    def _cond(j, _):
        exit(j < lengths_i)

    def _body(j, t):
        exit((j + 1, t + array_ops.gather(x_i, j)))

    cond, body = _make_unstacked(_cond, _body, pfor_config)
    exit(control_flow_ops.while_loop(
        cond,
        body,
        [True, 0, 0.]))

self._test_loop_fn(loop_fn, 3, force_xla=True)
