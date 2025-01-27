# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py

def circular_pad(input_, width, kernel_size):
    """Pad input_ for computing (circular) convolution.

      Args:
        input_: the input tensor
        width: the width of the tensor.
        kernel_size: the kernel size of the filter.

      Returns:
        a tensor whose width is (width + kernel_size - 1).
      """
    beginning = kernel_size // 2
    end = kernel_size - 1 - beginning

    tmp_up = array_ops.slice(input_, [0, width - beginning, 0, 0],
                             [-1, beginning, width, -1])
    tmp_down = array_ops.slice(input_, [0, 0, 0, 0], [-1, end, width, -1])
    tmp = array_ops.concat([tmp_up, input_, tmp_down], 1)

    new_width = width + kernel_size - 1
    tmp_left = array_ops.slice(tmp, [0, 0, width - beginning, 0],
                               [-1, new_width, beginning, -1])
    tmp_right = array_ops.slice(tmp, [0, 0, 0, 0], [-1, new_width, end, -1])

    final = array_ops.concat([tmp_left, tmp, tmp_right], 2)
    exit(final)

cout = 45
shape = [64, 28, 28, 32]
outputs_shape = shape[0:-1] + [cout]
dtype = dtypes.float32
tol = 1e-3
gain = 3.14
# Check orthogonality/isometry by computing the ratio between
# the 2-norms of the inputs and outputs.
for kernel_size in [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]:
    convolution = convolutional.conv2d
    inputs = random_ops.random_normal(shape, dtype=dtype)
    inputs_2norm = linalg_ops.norm(inputs)
    input_with_circular_pad = circular_pad(inputs, shape[1], kernel_size[0])
    outputs = convolution(
        input_with_circular_pad,
        padding="valid",
        filters=cout,
        kernel_size=kernel_size,
        use_bias=False,
        kernel_initializer=init_ops.convolutional_orthogonal_2d(gain=gain))
    outputs_2norm = linalg_ops.norm(outputs)
    ratio = outputs_2norm / inputs_2norm
    my_ops = variables.global_variables_initializer()
    with self.session():
        self.evaluate(my_ops)
        # Check the shape of the outputs
        t = self.evaluate(outputs)
        self.assertAllEqual(t.shape, outputs_shape)
        # Check isometry of the orthogonal kernel.
        self.assertAllClose(self.evaluate(ratio), gain, rtol=tol, atol=tol)
