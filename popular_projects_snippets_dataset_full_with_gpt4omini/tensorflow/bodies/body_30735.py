# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
with self.session():
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.placeholder(dtypes.float32)
    c = array_ops.concat([x, y], 2)

    output_shape = [10, 2, 9]
    grad_inp = np.random.rand(*output_shape).astype("f")
    grad_tensor = constant_op.constant(
        grad_inp.flatten(), shape=output_shape)

    grad = gradients_impl.gradients([c], [x, y], [grad_tensor])
    concated_grad = array_ops.concat(grad, 2)
    params = {
        x: np.random.rand(10, 2, 3).astype("f"),
        y: np.random.rand(10, 2, 6).astype("f")
    }
    result = concated_grad.eval(feed_dict=params)

    self.assertAllEqual(result, grad_inp)
