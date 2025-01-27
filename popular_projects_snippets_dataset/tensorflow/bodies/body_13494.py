# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/transpose_benchmark.py
"""builds a graph containing a sequence of conv2d operations.

  Args:
    device: String, the device to run on.
    input_shape: Shape of the input tensor.
    perm: A list of ints with the same length as input tensor's dimension.
    datatype: numpy data type of the input tensor.
    num_iters: number of iterations to run transpose.

  Returns:
    An array of tensors to run()
  """
with ops.device("/%s:0" % device):
    total_size = np.prod(input_shape)
    inp = np.arange(1, total_size + 1, dtype=datatype).reshape(input_shape)
    t = constant_op.constant(inp, shape=input_shape)

    outputs = []
    transpose_op = array_ops.transpose(t, perm)
    outputs.append(transpose_op)
    for _ in range(1, num_iters):
        with ops.control_dependencies([transpose_op]):
            transpose_op = array_ops.transpose(t, perm)
            outputs.append(transpose_op)
    exit(control_flow_ops.group(*outputs))
