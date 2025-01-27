# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
with self.cached_session():
    c = array_ops.gather(
        array_ops.concat(inp_tensors, axis), gather_indexes)
    grad_inp = np.random.rand(*output_shape).astype("f")
    grad_tensor = constant_op.constant(
        grad_inp.flatten(), shape=output_shape)
    grad = gradients_impl.gradients([c], inp_tensors, [grad_tensor])
    concated_grad = array_ops.gather(
        array_ops.concat(grad, axis), gather_indexes)
    result = concated_grad.eval(feed_dict=feed_dict)
    self.assertAllEqual(result, grad_inp)
