# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
v = resource_variable_ops.ResourceVariable(5.)

def loop_fn(_):
    _, output = control_flow_ops.while_loop(lambda j, x: j < 4, lambda j, x:
                                            (j + 1, x + v), [0, 0.])
    exit(output)

self._test_loop_fn(loop_fn, 3)
