# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
"""Verifies the output values of the pooling gradient function.

    Args:
      pool_func: Forward pooling function
      pool_grad_func: Pooling gradient function for pool_grad_func
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      pool_grad_grad_func: Second-order gradient function, if available.
    """
ksize = [1] + ksize + [1]
strides = [1] + strides + [1]
total_size = np.prod(input_sizes)
x = np.arange(1, total_size + 1, dtype=np.float32).reshape(input_sizes)
with self.session() as sess:
    # Use the forward pool function to compute some corresponding outputs
    # (needed for the CPU device, and we need the shape in both cases).
    with ops.device("CPU"):
        inputs = array_ops.placeholder(dtypes.float32, shape=input_sizes)
        outputs = pool_func(
            inputs,
            ksize=ksize,
            strides=strides,
            padding=padding)

    output_vals = np.array(sess.run(outputs, {inputs: x}))
    output_gradient_vals = np.arange(
        1, output_vals.size + 1, dtype=np.float32)
    output_gradient_vals = output_gradient_vals.reshape(output_vals.shape)
    output_grad_grad_vals = np.arange(1, x.size + 1, dtype=np.float32)
    output_grad_grad_vals = output_grad_grad_vals.reshape(x.shape)

    # Use the Tensorflow CPU pooling gradient to compute the expected input
    # gradients.
    with ops.device("CPU"):
        output_gradients = array_ops.placeholder(
            dtypes.float32, shape=output_vals.shape)
        expected_input_gradients = pool_grad_func(
            inputs,
            outputs,
            output_gradients,
            ksize=ksize,
            strides=strides,
            padding=padding)
        expected_input_gradient_vals = sess.run(
            expected_input_gradients,
            {inputs: x,
             output_gradients: output_gradient_vals})

        output_grad_gradients = array_ops.placeholder(
            dtypes.float32, shape=expected_input_gradient_vals.shape)
        if pool_grad_grad_func is not None:
            expected_grad_gradients = pool_grad_grad_func(
                inputs,
                outputs,
                output_grad_gradients,
                ksize=ksize,
                strides=strides,
                padding=padding,
                data_format="NDHWC")
            expected_grad_gradients_vals = sess.run(expected_grad_gradients, {
                inputs: x,
                output_grad_gradients: output_grad_grad_vals
            })

      # Run the gradient op on the XLA device
    with self.test_scope():
        outputs = array_ops.placeholder(dtypes.float32, shape=output_vals.shape)
        actual_input_gradients = pool_grad_func(
            inputs,
            outputs,
            output_gradients,
            ksize=ksize,
            strides=strides,
            padding=padding)
        if pool_grad_grad_func is not None:
            actual_grad_gradients = pool_grad_grad_func(
                inputs,
                outputs,
                output_grad_gradients,
                ksize=ksize,
                strides=strides,
                padding=padding,
                data_format="NDHWC")

    actual = sess.run(actual_input_gradients, {
        inputs: x,
        outputs: output_vals,
        output_gradients: output_gradient_vals
    })

    # Compare the Tensorflow and XLA results.
    self.assertAllClose(
        expected_input_gradient_vals.flatten(),
        actual.flatten(),
        rtol=1e-5,
        atol=1e-6)
    self.assertShapeEqual(actual, inputs)

    if pool_grad_grad_func is not None:
        actual_grad_gradients_vals = sess.run(
            actual_grad_gradients, {
                inputs: x,
                outputs: output_vals,
                output_grad_gradients: output_grad_grad_vals
            })

        # Compare the Tensorflow and XLA results.
        self.assertAllClose(
            expected_grad_gradients_vals,
            actual_grad_gradients_vals,
            rtol=1e-4,
            atol=1e-6)
        self.assertShapeEqual(actual_grad_gradients_vals, outputs)
