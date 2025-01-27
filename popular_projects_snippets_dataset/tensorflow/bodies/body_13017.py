# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/conv2d_benchmark.py
"""builds a graph containing a sequence of conv2d operations.

  Args:
    device: String, the device to run on.
    dtype: Data type for the convolution.
    data_format: A string from: "NHWC" or "NCHW". Data format for input and
                 output data.
    input_shape: Shape of the input tensor.
    filter_shape: Shape of the filter tensor.
    strides: A list of ints. 1-D of length 4. The stride of sliding
             window for each dimension of input.
    padding: A string from: "SAME", "VALID". The type of padding
             algorithm to use.
    num_iters: number of iterations to run conv2d.
    warmup_iters: number of iterations for warmup runs.

  Returns:
    An array of tensors to run()
  """
with ops.device("/%s:0" % device):
    inp = variables.VariableV1(
        random_ops.truncated_normal(input_shape, dtype=dtype))
    filt = variables.VariableV1(
        random_ops.truncated_normal(filter_shape, dtype=dtype))

    outputs = []
    conv2d_op = nn_ops.conv2d(
        inp, filt, strides, padding, data_format=data_format)
    outputs.append(conv2d_op)
    for _ in range(1, num_iters):
        with ops.control_dependencies([conv2d_op]):
            conv2d_op = nn_ops.conv2d(
                inp, filt, strides, padding, data_format=data_format)
            outputs.append(conv2d_op)

    warmup_groups = []
    warmup_conv2d_op = nn_ops.conv2d(
        inp, filt, strides, padding, data_format=data_format)
    warmup_groups.append(warmup_conv2d_op)
    for _ in range(1, warmup_iters):
        with ops.control_dependencies([warmup_conv2d_op]):
            warmup_conv2d_op = nn_ops.conv2d(
                inp, filt, strides, padding, data_format=data_format)
            warmup_groups.append(warmup_conv2d_op)
    exit((control_flow_ops.group(*warmup_groups), control_flow_ops.group(
        *outputs)))
