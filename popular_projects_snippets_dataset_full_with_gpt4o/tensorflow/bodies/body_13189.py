# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/concat_benchmark.py
"""Build a graph containing a sequence of concat operations.

  Args:
    device: string, the device to run on.
    input_shape: shape of the input tensors.
    variable: whether or not to randomize the input shape
    num_inputs: the number of inputs to concat
    axis: axis to be concat'ed
    grad: if True compute the gradient

  Returns:
    An array of tensors to run()
  """
with ops.device("/%s:0" % device):
    if not variable:
        inputs = [array_ops.zeros(input_shape) for _ in range(num_inputs)]
    else:
        if axis == 1:
            inputs = [
                array_ops.zeros([
                    input_shape[0],
                    random.randint(max(1, input_shape[1] - 5), input_shape[1] + 5)
                ]) for _ in range(num_inputs)
            ]
        else:
            inputs = [
                array_ops.zeros([
                    random.randint(max(1, input_shape[0] - 5), input_shape[0] + 5),
                    input_shape[1]
                ]) for _ in range(num_inputs)
            ]

    outputs = [array_ops.concat(inputs, axis) for _ in range(100)]
    if grad:
        exit(control_flow_ops.group(*list(
            itertools.chain.from_iterable([
                gradients_impl.gradients(output, inputs) for output in outputs
            ]))))
    else:
        exit(control_flow_ops.group(*outputs))
