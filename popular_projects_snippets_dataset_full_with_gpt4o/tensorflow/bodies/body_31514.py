# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Compare performance of EXPLICIT padding and calling tf.pad.

    A Conv2D op with EXPLICIT padding is benchmarked, and a tf.pad with the same
    padding followed by an equivalent Conv2D op is benchmarked.
    """
if not test.is_gpu_available():
    exit()

with ops.Graph().as_default():
    burn_iters = 15
    num_iters = 300
    batch_size = 64
    # The input and filter correspond to the first layer of Resnet50.
    input = variables.Variable(  # pylint: disable=redefined-builtin
        random_ops.random_uniform([
            batch_size,
            3,
            224,
            224
        ]))
    filter = variables.Variable(random_ops.random_uniform([7, 7, 3, 64]))  # pylint: disable=redefined-builtin
    strides = [1, 1, 2, 2]
    padding = [(0, 0), (0, 0), (3, 3), (3, 3)]
    output_explicit_pad = nn_ops.conv2d(
        input, filter, strides, padding=padding, data_format="NCHW")
    input_padded = array_ops.pad(input, padding)
    output_manual_pad = nn_ops.conv2d(
        input_padded, filter, strides, padding="VALID", data_format="NCHW")
    # Benchmark just the forward pass.
    self._bench_op("explicit_pad_forward", output_explicit_pad.op, burn_iters,
                   num_iters)
    self._bench_op("manual_pad_forward", output_manual_pad.op, burn_iters,
                   num_iters)

    # Benchmark both the forward and backwards passes.
    input_grad_explicit_pad, filter_grad_explicit_pad = (
        gradients_impl.gradients(output_explicit_pad, [input, filter]))
    self._bench_op(
        "explicit_pad_backward",
        control_flow_ops.group(input_grad_explicit_pad,
                               filter_grad_explicit_pad), burn_iters,
        num_iters)
    input_grad_manual_pad, filter_grad_manual_pad = gradients_impl.gradients(
        output_manual_pad, [input, filter])
    self._bench_op(
        "manual_pad_backward",
        control_flow_ops.group(input_grad_manual_pad, filter_grad_manual_pad),
        burn_iters, num_iters)
