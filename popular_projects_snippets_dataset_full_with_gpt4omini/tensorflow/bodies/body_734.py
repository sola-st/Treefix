# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
# Random dims of rank 5
input_shape = np.random.randint(1, 5, size=5)
# Random number of tensors
num_tensors = np.random.randint(1, 10)
# Random dim to concat on
concat_dim = np.random.randint(5)
concat_dim_sizes = np.random.randint(1, 5, size=num_tensors)
with self.session():
    inp = []
    inp_tensors = []
    with self.test_scope():
        for x in concat_dim_sizes:
            shape = input_shape
            shape[concat_dim] = x
            t = np.random.rand(*shape).astype("f")
            inp.append(t)
            inp_tensors.append(
                constant_op.constant(
                    [float(y) for y in t.flatten()],
                    shape=shape,
                    dtype=dtypes.float32))
        c = array_ops.concat(inp_tensors, concat_dim)
        output_shape = input_shape
        output_shape[concat_dim] = concat_dim_sizes.sum()
        grad_inp = np.random.rand(*output_shape).astype("f")
        grad_tensor = constant_op.constant(
            [float(x) for x in grad_inp.flatten()], shape=output_shape)
        grad = gradients_impl.gradients([c], inp_tensors, [grad_tensor])
        concated_grad = array_ops.concat(grad, concat_dim)
        result = self.evaluate(concated_grad)

self.assertAllEqual(result, grad_inp)
