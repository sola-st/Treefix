# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(pfor_control_flow_ops.pfor(lambda i: f(array_ops.gather(x, i)),
                                  array_ops.shape(x)[0]))
