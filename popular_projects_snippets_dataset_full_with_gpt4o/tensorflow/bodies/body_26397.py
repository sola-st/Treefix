# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
i = constant_op.constant(0)

def body(i, x):
    exit((math_ops.add(i, 1), x))

exit(control_flow_ops.while_loop(math_ops.less, body, [i, x]))
