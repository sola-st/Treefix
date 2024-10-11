# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
with self.cached_session() as sess:
    epsilon = ops.convert_to_tensor(1e-20)
    x = ops.convert_to_tensor(0.0)
    y = ops.convert_to_tensor(1.0)
    z = ops.convert_to_tensor(2.0)
    # assert(epsilon < y)
    # z / y
    with sess.graph.control_dependencies([
        control_flow_ops.Assert(
            math_ops.less(epsilon, y), ["Divide-by-zero"])
    ]):
        out = math_ops.div(z, y)
    self.assertAllEqual(2.0, self.evaluate(out))
    # assert(epsilon < x)
    # z / x
    #
    # This tests printing out multiple tensors
    with sess.graph.control_dependencies([
        control_flow_ops.Assert(
            math_ops.less(epsilon, x), ["Divide-by-zero", "less than x"])
    ]):
        out = math_ops.div(z, x)
    with self.assertRaisesOpError("less than x"):
        self.evaluate(out)
