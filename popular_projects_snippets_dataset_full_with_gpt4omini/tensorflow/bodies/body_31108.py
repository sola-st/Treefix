# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_transpose_test.py
# `NCHW` data format is only supported for CUDA device.
if test.is_gpu_available(cuda_only=True):
    with self.session():
        strides = [1, 1, 1, 1]

        # Input, output: [batch, depth, height, width, depth]
        x_shape = [2, 3, 6, 4]
        y_shape = [2, 2, 6, 4]

        # Filter: [kernel_height, kernel_width, output_depth, input_depth]
        f_shape = [3, 3, 2, 3]

        x = constant_op.constant(
            1.0, shape=x_shape, name="x", dtype=dtypes.float32)
        f = constant_op.constant(
            1.0, shape=f_shape, name="filter", dtype=dtypes.float32)

        output = nn_ops.conv2d_transpose(
            x, f, y_shape, strides=strides, padding="SAME", data_format="NCHW")

        value = self.evaluate(output)
        for n in range(x_shape[0]):
            for k in range(f_shape[2]):
                for w in range(y_shape[3]):
                    for h in range(y_shape[2]):
                        target = 4 * 3.0
                        h_in = h > 0 and h < y_shape[2] - 1
                        w_in = w > 0 and w < y_shape[3] - 1
                        if h_in and w_in:
                            target += 5 * 3.0
                        elif h_in or w_in:
                            target += 2 * 3.0
                        self.assertAllClose(target, value[n, k, h, w])
