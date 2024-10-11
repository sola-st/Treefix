# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
with self.session():
    inp = []
    inp_tensors = []
    with self.test_scope():
        for x in [1, 2, 6]:
            shape = [x, 10, 2]
            t = np.random.rand(*shape).astype("f")
            inp.append(t)
            inp_tensors.append(
                constant_op.constant(
                    [float(y) for y in t.flatten()],
                    shape=shape,
                    dtype=dtypes.float32))
        c = array_ops.concat(inp_tensors, 0)
        output_shape = [9, 10, 2]
        grad_inp = np.random.rand(*output_shape).astype("f")
        grad_tensor = constant_op.constant(
            [float(x) for x in grad_inp.flatten()], shape=output_shape)
        grad = gradients_impl.gradients([c], inp_tensors, [grad_tensor])
        concated_grad = array_ops.concat(grad, 0)
        result = self.evaluate(concated_grad)

self.assertAllEqual(result, grad_inp)
