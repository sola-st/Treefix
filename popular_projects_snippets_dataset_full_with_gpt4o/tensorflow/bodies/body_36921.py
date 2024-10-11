# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
enqueue_print_op("A")
enqueue_print_op("B")
with ops.control_dependencies([enqueue_print_op("C")]):
    exit(constant_op.constant(10))
