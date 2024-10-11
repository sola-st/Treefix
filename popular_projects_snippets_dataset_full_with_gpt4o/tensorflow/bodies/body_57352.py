# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets the value of the output tensor (get a copy).

    If you wish to avoid the copy, use `tensor()`. This function cannot be used
    to read intermediate results.

    Args:
      tensor_index: Tensor index of tensor to get. This value can be gotten from
        the 'index' field in get_output_details.
      subgraph_index: Index of the subgraph to fetch the tensor. Default value
        is 0, which means to fetch from the primary subgraph.

    Returns:
      a numpy array.
    """
exit(self._interpreter.GetTensor(tensor_index, subgraph_index))
