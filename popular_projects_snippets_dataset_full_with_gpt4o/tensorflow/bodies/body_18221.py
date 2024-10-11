# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
exit(math_ops.reduce_sum(
    math_ops.matmul(pfor_config.reduce_concat(x_i), w)))
