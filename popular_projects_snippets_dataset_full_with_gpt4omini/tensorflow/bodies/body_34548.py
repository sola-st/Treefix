# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
np_dtype = dtype.as_numpy_dtype
with self.cached_session():

    def func(v0, state0, var):
        ta = tensor_array_ops.TensorArray(
            dtype=dtype,
            tensor_array_name="foo",
            size=0 if dynamic_size else 3,
            dynamic_size=dynamic_size)
        time_0 = array_ops.identity(0)

        def body(time, ta_t, state):
            sliced = array_ops.slice(
                v0, begin=array_ops.stack([time, 0]), size=[1, -1])
            sliced = array_ops.squeeze(sliced)
            out = sliced + var + state
            state += sliced
            ta_t = ta_t.write(time, out)
            exit((time + 1, ta_t, state))

        (unused_0, h_final, unused_2) = control_flow_ops.while_loop(
            cond=lambda time, unused_1, unused_2: time < 3,
            body=body,
            loop_vars=(time_0, ta, state0),
            shape_invariants=(time_0.get_shape(), tensor_shape.unknown_shape(),
                              tensor_shape.unknown_shape()),
            parallel_iterations=3)
        vout = h_final.stack()
        exit(vout)

    v0 = array_ops.identity(np.arange(3 * 5, dtype=np_dtype).reshape(3, 5))
    state0 = array_ops.identity(np.array([1] * 5, dtype=np_dtype))
    init_val = np.arange(100, 105, dtype=np_dtype)
    var = variable_scope.get_variable(
        "var",
        shape=init_val.shape,
        dtype=np_dtype,
        initializer=init_ops.constant_initializer(init_val))

    vout = func(v0, state0, var)
    grad_val = -np.arange(3 * 5, dtype=np_dtype).reshape(3, 5)
    if context.executing_eagerly():
        grad_fn = backprop.gradients_function(func)
        v0_grad, state0_grad, var_grad = grad_fn(v0, state0, var, dy=grad_val)
    else:
        v0_grad = gradients_impl.gradients([vout], [v0], [grad_val])[0]
        state0_grad = gradients_impl.gradients([vout], [state0], [grad_val])[0]
        var_grad = gradients_impl.gradients([vout], [var], [grad_val])[0]
        self.evaluate(variables.global_variables_initializer())

    state0_t, var_t, v0_t, vout_t, v0_grad_t, var_grad_t, state0_grad_t = (
        self.evaluate(
            ([state0, var, v0, vout, v0_grad, var_grad, state0_grad])))
    just_v0_grad_t = self.evaluate(v0_grad)

    # state = [ state0 | state0 + v0[0] | state0 + v0[0] + v0[1] ]
    # vout = [ v0[0] + var + state[0] |
    #          v0[1] + var + state[1] |
    #          v0[2] + var + state[2] ]
    #      = [ v0[0] + var + state0 |
    #          v0[1] + var + state0 + v0[0] |
    #          v0[2] + var + state0 + v0[0] + v0[1] ]
    #
    # d(vout[0])/d(v0) = [1 | 0 | 0 ]
    # d(vout[1])/d(v0) = [1 | 1 | 0 ]
    # d(vout[2])/d(v0) = [1 | 1 | 1 ]
    # d(vout)/d(var) = [1 | 1 | 1]
    # d(vout)/d(state0) = [ 1 | 1 | 1 ]

    state_per_time = np.array(
        [state0_t, state0_t + v0_t[0, :], state0_t + v0_t[0, :] + v0_t[1, :]])

    # Compare forward prop
    self.assertAllClose(v0_t + var_t + state_per_time, vout_t)

    # Compare backward prop
    expected_v0_grad_t = np.array([
        grad_val[0, :] + grad_val[1, :] + grad_val[2, :],
        grad_val[1, :] + grad_val[2, :], grad_val[2, :]
    ])

    self.assertAllEqual(expected_v0_grad_t, v0_grad_t)
    self.assertAllEqual(expected_v0_grad_t, just_v0_grad_t)
    self.assertAllClose(grad_val.sum(axis=0), var_grad_t)
    self.assertAllClose(grad_val.sum(axis=0), state0_grad_t)
