# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
exit(cond_v2.cond_v2(x_i < y, lambda: z - x_i, lambda: z + x_i))
