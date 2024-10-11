# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
# Test both positive and negative concat axis.
# -1 and 2 correspond to the same axis for 3-dimensional tensors.
for axis in [-1, 2]:
    with test_util.use_gpu():
        inp = []
        inp_tensors = []
        for x in [1, 2, 6]:
            shape = [10, 2, x]
            t = np.random.rand(*shape).astype("f")
            inp.append(t)
            inp_tensors.append(
                constant_op.constant(
                    t.flatten(),
                    shape=shape,
                    dtype=dtypes.float32))
        c = array_ops.concat(inp_tensors, 2)
        output_shape = [10, 2, 9]
        grad_inp = np.random.rand(*output_shape).astype("f")
        grad_tensor = constant_op.constant(
            grad_inp.flatten(), shape=output_shape)
        grad = gradients_impl.gradients([c], inp_tensors, [grad_tensor])
        concated_grad = array_ops.concat(grad, axis)
        result = self.evaluate(concated_grad)

self.assertAllEqual(result, grad_inp)
