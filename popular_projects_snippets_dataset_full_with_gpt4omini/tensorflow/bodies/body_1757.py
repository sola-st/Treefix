# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
"""Verifies the output values of the pooling gradient function.

    Args:
      pool_func: Forward pooling function
      pool_grad_func: Pooling gradient function for pool_grad_func
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      data_format: The data format we use to run the pooling operation.
      pool_grad_grad_func: Second-order gradient function, if available.
    """
total_size = np.prod(input_sizes)
# TODO(b/73062247): MaxPoolGradGrad can confuse gradients when x is equally
# maximal at 16 bits. Switch to np.random.randn when resolved.
x = np.arange(1, total_size + 1, dtype=np.float32)
x *= (np.random.randint(2, size=total_size) * 2 - 1)  # Flip signs randomly
# Verify some specifically interesting values...
x[np.random.choice(total_size)] = np.inf
x[np.random.choice(total_size)] = -np.inf
# TODO(b/74222344): Fix nan handling for max pool grad.
# x[np.random.choice(total_size)] = np.nan
x = x.reshape(input_sizes)
with self.session() as sess:
    # Use the forward pool function to compute some corresponding outputs
    # (needed for the CPU device, and we need the shape in both cases).
    with ops.device(self.CPU_DEVICE):
        inputs = array_ops.placeholder(dtypes.float32, shape=input_sizes)
        outputs = pool_func(
            inputs,
            ksize=ksize,
            strides=strides,
            padding=padding,
            data_format="NHWC")

    output_vals = np.array(sess.run(outputs, {inputs: x}))
    output_gradient_vals = np.arange(
        1, output_vals.size + 1, dtype=np.float32)
    output_gradient_vals = output_gradient_vals.reshape(output_vals.shape)
    output_grad_grad_vals = np.arange(1, x.size + 1, dtype=np.float32)
    output_grad_grad_vals = output_grad_grad_vals.reshape(x.shape)

    # Use the Tensorflow CPU pooling gradient to compute the expected input
    # gradients.
    with ops.device(self.CPU_DEVICE):
        output_gradients = array_ops.placeholder(
            dtypes.float32, shape=output_vals.shape)
        expected_input_gradients = pool_grad_func(
            inputs,
            outputs,
            output_gradients,
            ksize=ksize,
            strides=strides,
            padding=padding,
            data_format="NHWC")
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
                data_format="NHWC")
            expected_grad_gradients_vals = sess.run(expected_grad_gradients, {
                inputs: x,
                output_grad_gradients: output_grad_grad_vals
            })

      # Run the gradient op on the XLA device
    with self.test_scope():
        outputs = array_ops.placeholder(dtypes.float32, shape=output_vals.shape)
        xla_inputs = inputs
        xla_outputs = outputs
        xla_output_gradients = output_gradients
        xla_output_grad_gradients = output_grad_gradients
        xla_ksize = ksize
        xla_strides = strides
        if data_format == "NCHW":
            xla_inputs = NHWCToNCHW(inputs)
            xla_outputs = NHWCToNCHW(outputs)
            xla_output_gradients = NHWCToNCHW(output_gradients)
            xla_output_grad_gradients = NHWCToNCHW(output_grad_gradients)
            xla_ksize = NHWCToNCHW(ksize)
            xla_strides = NHWCToNCHW(strides)
        actual_input_gradients = pool_grad_func(
            xla_inputs,
            xla_outputs,
            xla_output_gradients,
            ksize=xla_ksize,
            strides=xla_strides,
            padding=padding,
            data_format=data_format)
        if data_format == "NCHW":
            actual_input_gradients = NCHWToNHWC(actual_input_gradients)
        if pool_grad_grad_func is not None:
            actual_grad_gradients = pool_grad_grad_func(
                xla_inputs,
                xla_outputs,
                xla_output_grad_gradients,
                ksize=xla_ksize,
                strides=xla_strides,
                padding=padding,
                data_format=data_format)
            if data_format == "NCHW":
                actual_grad_gradients = NCHWToNHWC(actual_grad_gradients)
    actual_input_gradients_vals = sess.run(actual_input_gradients, {
        inputs: x,
        outputs: output_vals,
        output_gradients: output_gradient_vals
    })
    # Compare the Tensorflow and XLA results.
    self.assertAllClose(
        expected_input_gradient_vals,
        actual_input_gradients_vals,
        rtol=1e-4,
        atol=1e-6)
    self.assertShapeEqual(actual_input_gradients_vals, inputs)

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
