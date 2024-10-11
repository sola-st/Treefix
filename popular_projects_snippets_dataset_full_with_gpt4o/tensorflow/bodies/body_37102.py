# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(control_flow_ops.while_loop(
    lambda j, _: j < 3,
    lambda j, y: (j + 1,
                  y + math_ops.reduce_sum(var.sparse_read([1, 2]))),
    [0, x])[1])
