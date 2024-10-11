# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
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
