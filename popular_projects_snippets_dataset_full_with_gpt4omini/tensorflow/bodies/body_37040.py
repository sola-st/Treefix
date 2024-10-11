# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    n = ops.convert_to_tensor(0)
    c = lambda x: math_ops.less(x, 10)
    # pylint: disable=undefined-variable
    # for OSS build
    b = lambda x: control_flow_ops.cond(math_ops.less(0, 1),
                                        lambda: math_ops.add(x, 1),
                                        lambda: math_ops.subtract(x, 1))
    # pylint: enable=undefined-variable
    r = control_flow_ops.while_loop(c, b, [n])
    self.assertAllEqual(10, self.evaluate(r))
