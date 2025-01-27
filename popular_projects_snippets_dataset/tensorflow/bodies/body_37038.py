# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    i = ops.convert_to_tensor(0, name="i")
    n = ops.convert_to_tensor(10, name="n")
    one = ops.convert_to_tensor(1, name="one")
    c = lambda x: math_ops.less(x, n)
    # pylint: disable=undefined-variable
    # for OSS build
    b = lambda x: control_flow_ops.cond(
        constant_op.constant(True),
        lambda: math_ops.add(x, one), lambda: math_ops.subtract(x, one))
    # pylint: enable=undefined-variable
    r = control_flow_ops.while_loop(c, b, [i])
    self.assertAllEqual(10, self.evaluate(r))
