# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
vectorized_value = pfor_config.reduce_concat(x_i)
mean_value = math_ops.reduce_mean(vectorized_value, axis=0)
exit(x_i - mean_value)
