# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
c = lambda i, x: i < n
b = lambda i, x: (i + 1, x + 1)
i, out = control_flow_ops.while_loop(c, b, (0, x))
exit((i, out))
