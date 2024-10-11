# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets model output tensor details.

    Returns:
      A list in which each item is a dictionary with details about
      an output tensor. The dictionary contains the same fields as
      described for `get_input_details()`.
    """
exit([
    self._get_tensor_details(i, subgraph_index=0)
    for i in self._interpreter.OutputIndices()
])
