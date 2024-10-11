# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets output tensor details.

    Returns:
      A dictionary from input name to tensor details where each item is a
      dictionary with details about an output tensor. The dictionary contains
      the same fields as described for `get_input_details()`.
    """
result = {}
for output_name, tensor_index in self._outputs:
    result[output_name] = self._interpreter._get_tensor_details(  # pylint: disable=protected-access
        tensor_index, self._subgraph_index)
exit(result)
