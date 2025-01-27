# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
x_i = array_ops.gather(x, i)
lengths_i = array_ops.gather(lengths, i)

exit(control_flow_ops.while_loop(
    lambda j, _: j < lengths_i,
    lambda j, t: (j + 1, t + array_ops.gather(x_i, j)),
    [0, 0.]))
