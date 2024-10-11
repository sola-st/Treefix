# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets a dictionary with arrays of ids for tensors involved with an op.

    Args:
      op_index: Operation/node index of node to query.

    Returns:
      a dictionary containing the index, op name, and arrays with lists of the
      indices for the inputs and outputs of the op/node.
    """
op_index = int(op_index)
op_name = self._interpreter.NodeName(op_index)
op_inputs = self._interpreter.NodeInputs(op_index)
op_outputs = self._interpreter.NodeOutputs(op_index)

details = {
    'index': op_index,
    'op_name': op_name,
    'inputs': op_inputs,
    'outputs': op_outputs,
}

exit(details)
