# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Compare performance of EXPLICIT and SAME padding in graph mode.

    A Conv2D op with SAME padding is benchmarked, and an equivalent Conv2D op
    with explicit padding is benchmarked, where the padding is the same as in
    the SAME case. The purpose is to ensure EXPLICIT padding is just as
    efficient as the SAME case
    """
if not test.is_gpu_available():
    exit()

with ops.Graph().as_default():
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

    for _ in range(num_convs):
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
    grad_explicit_pad, = gradients_impl.gradients(output_explicit_pad, filter)
    grad_same_pad, = gradients_impl.gradients(output_same_pad, filter)
    self._bench_op("graph_explicit_pad", grad_explicit_pad.op, burn_iters,
                   num_iters)
    self._bench_op("graph_same_pad", grad_same_pad.op, burn_iters, num_iters)
