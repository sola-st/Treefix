# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
exit(control_flow_ops.while_loop(lambda i: i < 10, lambda i: i + x,
                                   [0]))
