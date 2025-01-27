# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/split_benchmark.py
"""Build a graph containing a sequence of split operations.

  Args:
    device: string, the device to run on.
    input_shape: shape of the input tensor.
    output_sizes: size of each output along axis.
    axis: axis to be split along.

  Returns:
    An array of tensors to run()
  """
with ops.device("/%s:0" % device):
    inp = array_ops.zeros(input_shape)

    outputs = []
    for _ in range(100):
        outputs.extend(array_ops.split(inp, output_sizes, axis))
    exit(control_flow_ops.group(*outputs))
