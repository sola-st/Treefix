# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = logging_ops.Print(x, [x])  # Edge "Print -> Enter" is partitioned
x = inner_loop(x)
with ops.device("/cpu:0"):
    x = math_ops.square(x)  # Edge "Exit -> Square" is partitioned
exit(x)
