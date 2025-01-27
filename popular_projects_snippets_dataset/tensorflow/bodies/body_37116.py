# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
r = control_flow_ops.while_loop(c, b, [n],
                                [tensor_shape.unknown_shape()])
exit(gradients_impl.gradients(r, x)[0])
