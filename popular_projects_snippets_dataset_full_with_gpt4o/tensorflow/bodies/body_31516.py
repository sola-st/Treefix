# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Compare performance of EXPLICIT and SAME padding in eager mode.

    A Conv2D op with SAME padding is benchmarked, and an equivalent Conv2D op
    with explicit padding is benchmarked, where the padding is the same as in
    the SAME case. Currently, EXPLICIT padding is slightly slower, due to the
    fact the Python padding list must be checked and processed before the Conv2D
    op can run.
    """
# TODO(reedwm): Make EXPLICIT padding as fast as SAME padding.
if not test.is_gpu_available():
    exit()

with context.eager_mode():
    burn_iters = 15
    num_convs = 20
    num_iters = 50
    batch_size = 64
    # The input and filter correspond to a middle layer of Resnet50.
    input = variables.Variable(  # pylint: disable=redefined-builtin
        random_ops.random_uniform([
            batch_size,
            256,
            14,
            14
        ]))
    filter = variables.Variable(random_ops.random_uniform([3, 3, 256, 256]))  # pylint: disable=redefined-builtin
    strides = [1, 1, 1, 1]
    padding = [(0, 0), (0, 0), (1, 1), (1, 1)]
    output_explicit_pad = input
    output_same_pad = input
    for _ in range(burn_iters):
        output_explicit_pad = nn_ops.conv2d(
            output_explicit_pad,
            filter,
            strides,
            padding=padding,
            data_format="NCHW")
        output_same_pad = nn_ops.conv2d(
            output_same_pad,
            filter,
            strides,
            padding="SAME",
            data_format="NCHW")

    start = time.time()
    for _ in range(num_iters):
        with backprop.GradientTape() as tape:
            for _ in range(num_convs):
                output_explicit_pad = nn_ops.conv2d(
                    output_explicit_pad,
                    filter,
                    strides,
                    padding=padding,
                    data_format="NCHW")
            tape.gradient(output_explicit_pad, filter)
    end = time.time()
    self.report_benchmark(
        name="eager_explicit_pad",
        wall_time=(end - start) / num_iters,
        iters=num_iters)

    start = time.time()
    for _ in range(num_iters):
        with backprop.GradientTape() as tape:
            for _ in range(num_convs):
                output_same_pad = nn_ops.conv2d(
                    output_same_pad,
                    filter,
                    strides,
                    padding="SAME",
                    data_format="NCHW")
            tape.gradient(output_same_pad, filter)
    end = time.time()
    self.report_benchmark(
        name="eager_same_pad",
        wall_time=(end - start) / num_iters,
        iters=num_iters)
