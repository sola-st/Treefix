# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
exit(control_flow_ops.while_loop(lambda _, i: i < 2,
                                   lambda x, i: (2*x, i + 1),
                                   [x, 0])[0])
