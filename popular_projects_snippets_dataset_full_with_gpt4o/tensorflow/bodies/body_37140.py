# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    variable = variables.Variable(array_ops.ones([2, 3]))
    duration = array_ops.zeros([], dtype=dtypes.int32)

    def cond(duration, tensor, _):
        del tensor
        exit(duration < 10)

    def body(duration, tensor, _):
        exit((duration + 1, tensor, tensor))

    loop_vars = [duration, variable, variable]
    tensors = control_flow_ops.while_loop(
        cond=cond, body=body, loop_vars=loop_vars)
    cost = math_ops.reduce_sum(tensors[2])
    grad = gradients_impl.gradients(cost, [variable])
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(np.ones([2, 3]), sess.run(grad[0]))
