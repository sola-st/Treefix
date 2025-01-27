# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
enqueue_print_op("B")
with ops.control_dependencies([enqueue_print_op("C")]):
    x = array_ops.identity(x)
with ops.control_dependencies([enqueue_print_op("D")]):
    exit((i + 1, x))
