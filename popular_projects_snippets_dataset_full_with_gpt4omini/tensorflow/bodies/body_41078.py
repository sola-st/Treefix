# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
c = lambda n: n < 10
b = lambda n: n * x
exit(control_flow_ops.while_loop(c, b, [n],
                                   [tensor_shape.unknown_shape()]))
