# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
gain = 3.14
for dtype in [dtypes.float32]:
    for kernel_size in [[3], [8], [3, 5], [2, 4], [3, 3, 3], [2, 2, 2]]:
        tol = 1e-2
        # Check orthogonality by computing ratio between
        # the 2-norms of the inputs and outputs.
        if len(kernel_size) == 1:
            shape = [4, 32, 64]
            convolution = convolutional.conv1d
        elif len(kernel_size) == 2:
            convolution = convolutional.conv2d
            shape = [4, 32, 32, 64]
        else:
            shape = [4, 16, 16, 16, 64]
            convolution = convolutional.conv3d
        inputs = random_ops.random_normal(shape, dtype=dtype)
        inputs_2norm = linalg_ops.norm(inputs)
        outputs = convolution(
            inputs,
            padding="same",
            filters=128,
            kernel_size=kernel_size,
            use_bias=False,
            kernel_initializer=init_ops.convolutional_delta_orthogonal(
                gain=gain))
        outputs_shape = shape[0:-1] + [128]
        outputs_2norm = linalg_ops.norm(outputs)
        ratio = outputs_2norm / inputs_2norm
        my_ops = variables.global_variables_initializer()
        with self.session():
            self.evaluate(my_ops)
            # Check the shape of the outputs
            t = self.evaluate(outputs)
            self.assertAllEqual(t.shape, outputs_shape)
            # Check isometry of the delta-orthogonal kernel.
            self.assertAllClose(self.evaluate(ratio), gain, rtol=tol, atol=tol)
