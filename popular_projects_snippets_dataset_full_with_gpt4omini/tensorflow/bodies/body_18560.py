# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
x_i = array_ops.gather(x, i)
exit(x_i - pfor_config.reduce_mean(x_i))
