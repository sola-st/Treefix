# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
inp = array_ops.gather(x, i)
output = pfor_control_flow_ops.vectorized_map(compute, inp)
output.set_shape([5, 1])
exit(output)
