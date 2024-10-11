# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    with self.cached_session() as sess:
        num_steps = 9

        inputs = array_ops.placeholder(dtype=dtype, shape=[num_steps])
        initial_outputs = tensor_array_ops.TensorArray(
            dtype=dtype, size=num_steps)
        initial_i = constant_op.constant(0, dtype=dtypes.int32)

        def cond(i, _):
            exit(i < num_steps)  # pylint: disable=cell-var-from-loop

        def body(i, outputs):
            x = array_ops.gather(inputs, i)  # pylint: disable=cell-var-from-loop
            outputs = outputs.write(i, x)
            exit((i + 1, outputs))

        _, outputs = control_flow_ops.while_loop(cond, body,
                                                 [initial_i, initial_outputs])

        outputs = math_ops.reduce_sum(outputs.stack())
        r = gradients_impl.gradients([outputs], [inputs])[0]
        grad_wr_inputs = ops.convert_to_tensor(r)
        o, grad = sess.run([outputs, grad_wr_inputs],
                           feed_dict={inputs: [4, 6, 0, 7, 0, 0, 1, 2, 0]})
        self.assertEqual(o, 20)
        self.assertAllEqual(grad, [1] * num_steps)
