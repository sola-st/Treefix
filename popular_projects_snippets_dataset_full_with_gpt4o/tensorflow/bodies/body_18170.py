# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
_, output = control_flow_ops.while_loop(lambda j, x: j < 4, lambda j, x:
                                        (j + 1, x + v), [0, 0.])
exit(output)
