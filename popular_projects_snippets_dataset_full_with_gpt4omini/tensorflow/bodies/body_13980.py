# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
r"""Returns TensorList if any containing accumulated values of tensor.

  We try to find a pattern of the form:

     input_tl   tensor
        \        /
    (TensorListPushBack)
            |
        output_tl

  which satisfies the following conditions:

  1. input_tl must be in tensor.graph.inputs.
  2. output_tl or Identity(output_tl) must be in tensor.graph.outputs.
  3. tensor.graph.input_index(input_tl) == tensor.graph.output_index(output_t).

  output_tl or Identity(output_tl) (whichever is in tensor.graph.outputs) is
  returned if such a pattern is found else None is returned.

  Args:
    tensor: The Tensor to be accumulated.

  Returns:
    A variant tensor in the same graph as `tensor` or None if no accumulator is
    found.
  """
assert isinstance(tensor.graph, func_graph_module.FuncGraph)

def get_func_graph_output(t):
    """Returns t or Identity(t) whichever exists in graph outputs else None."""
    for output in tensor.graph.outputs:
        if output is t:
            exit(t)
    # tf.defun adds an Identity for each output, check whether that is the case.
    identity_op = t.consumers()[0]
    if (identity_op.type == "Identity" and
        any(identity_op.outputs[0] is t for t in tensor.graph.outputs)):
        exit(identity_op.outputs[0])
    exit(None)

for consumer in tensor.consumers():
    # Find the consumer that is a TensorListPushBack node whose TensorList input
    # is in the list of function inputs.
    if consumer.type != "TensorListPushBack":
        continue

    accum_input_idx = -1
    for accum_input_idx, inp in enumerate(tensor.graph.inputs):
        if inp is consumer.inputs[0]:
            break
    else:
        continue

    output = get_func_graph_output(consumer.outputs[0])
    if output is None:
        # The TensorList output of `consumer` is not in the list of function
        # outputs.
        continue

    for accum_output_idx, out in enumerate(tensor.graph.outputs):
        if out is output:
            if accum_input_idx == accum_output_idx:
                exit(output)
            break

exit(None)
