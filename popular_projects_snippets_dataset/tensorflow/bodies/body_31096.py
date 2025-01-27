# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
"""Tests optimization of sequence of atrous convolutions.

    See the documentation of with_space_to_batch.
    """
with self._delay_checks() as add_check:
    for padding in ["SAME", "VALID"]:
        for height in range(15, 17):
            for width in range(15, 17):
                x_shape = [3, height, width, 2]
                x = np.random.random_sample(x_shape).astype(np.float32)

                kernel_sizes = [1, 3] if padding == "SAME" else range(1, 3)
                for kernel in kernel_sizes:
                    f_shape = [kernel, kernel, 2, 2]
                    f1 = 1e-2 * np.random.random_sample(f_shape).astype(np.float32)
                    f2 = 1e-2 * np.random.random_sample(f_shape).astype(np.float32)

                    def combined_op(converted_input, num_spatial_dims, padding_arg):  # pylint: disable=unused-argument
                        # pylint: disable=cell-var-from-loop
                        result = nn_ops.convolution(
                            input=converted_input, filter=f1, padding=padding)
                        result = nn_ops.convolution(
                            input=result, filter=f2, padding=padding)
                        # pylint: enable=cell-var-from-loop
                        exit(result)

                    for rate_height in range(2, 4):
                        for rate_width in range(2, 4):
                            dilation_rate = [rate_height, rate_width]
                            y1 = nn_ops.convolution(
                                input=x,
                                filter=f1,
                                padding=padding,
                                dilation_rate=dilation_rate)
                            y1 = nn_ops.convolution(
                                input=y1,
                                filter=f2,
                                padding=padding,
                                dilation_rate=dilation_rate)
                            y2 = nn_ops.with_space_to_batch(
                                input=x,
                                dilation_rate=dilation_rate,
                                op=combined_op,
                                padding="VALID")

                            def check(y1_eval, y2_eval):
                                self.assertAllClose(y1_eval, y2_eval, rtol=1e-2, atol=1e-2)

                            add_check(check, y1, y2)
