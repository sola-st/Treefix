# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x1 = array_ops.gather(x, i)
exit(logging_ops.Print(
    x1, [x1, "x1", array_ops.shape(x1)], summarize=10))
